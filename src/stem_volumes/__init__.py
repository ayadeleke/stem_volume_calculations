"""This module implements a command to apply the stem volume to a CSV file."""
import argparse
import cProfile
import os
import pstats
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from functools import lru_cache, partial
from inspect import signature

import numpy as np
import pandas as pd
from functools import partial


from line_profiler import LineProfiler

import stem_volumes.formulas
from stem_volumes.utils import (
    convert_volume_to_m3,
    extract_parameter_units,
    extract_volume_unit,
    clean_data,
    match_species_names,
    get_genus_row_map
)
from stem_volumes.genus_dict import genus_species_common_dict


def __orig_main():
    pr = cProfile.Profile()
    pr.enable()
    tic = time.perf_counter()
    args = parse_arguments()

    if os.path.exists(args.output_file):
        print(f'Error: {args.output_file} already exists.', file=sys.stderr)
        print(
            f"This script won't overwrite it to avoid accidental data loss.",
            file=sys.stderr,
        )
        sys.exit(1)

    toc = time.perf_counter()
    print(f'Parsing arguments took {toc - tic:.6f} seconds')
    tic = toc

    df = pd.read_csv(args.csv_file)
    toc = time.perf_counter()
    print(f'Reading CSV file took {toc - tic:.6f} seconds')
    tic = toc

    df_cleaned = clean_data(df)
    toc = time.perf_counter()
    print(f'Cleaning the CSV file took {toc - tic:.6f} seconds')
    tic = toc

    df_calculated = calculate_stem_volumes(df_cleaned)
    toc = time.perf_counter()
    print(f'Calculating the volumes took {toc - tic:.6f} seconds')
    tic = toc

    df_calculated.to_csv(args.output_file, index=False)
    toc = time.perf_counter()
    print(f'Writing the CSV file took {toc - tic:.6f} seconds')

    pr.disable()
    stats = pstats.Stats(pr)
    stats.sort_stats('cumtime').print_stats(10)


def main():
    """Main function."""
    profiler = LineProfiler()
    profiler.add_function(calculate_stem_volumes)
    profiler.add_function(__orig_main)
    profiler_wrapper = profiler(__orig_main)
    profiler_wrapper()
    profiler.print_stats()


def parse_arguments():
    """Parses the arguments, i.e., CSV input and output file."""
    parser = argparse.ArgumentParser(
        description='Calculate stem volumes for given CSV file'
    )

    parser.add_argument(
        'csv_file', help='Path to CSV file, e.g., path/to/test.csv.'
    )
    parser.add_argument(
        'output_file', help='Path to CSV file to save the added results in.'
    )
    return parser.parse_args()


@lru_cache(maxsize=1000)
def _apply_formula_cached(formula_func, params, parameter_units, volume_unit, diameter_mm, height_dm):
    """Cached version of formula application to avoid redundant calculations."""
    if pd.isna(diameter_mm) or (len(params) > 1 and pd.isna(height_dm)):
        return pd.NA

    UNITS = {
        'D': ['mm', 'cm', 'dm', 'm'],
        'H': ['dm', 'm'],
    }

    args = {'D': diameter_mm, 'H': height_dm}
    try:
        converted_args = [
            args[par_name] / 10 ** UNITS[par_name].index(parameter_units[i])
            for i, par_name in enumerate(params)
        ]
        volume = formula_func(*converted_args)
        return convert_volume_to_m3(volume, volume_unit)
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        return pd.NA

def calculate_stem_volumes(df):
    """Applies genus-specific stem volume formulas to the data, keeping all 230 columns."""
    result_df = df.copy()
    result_df['genus'] = match_species_names(result_df)  # Add genus column
    result_df[['genus', 'species']] = pd.DataFrame(
        result_df['genus'].tolist(), index=result_df.index
    )
    result_df['genus'] = result_df['genus'].astype(str).str.strip().str.capitalize()

    # Step 1: Get all formulas (1–230) into a lookup dict
    all_formulas = {}
    for formula_no in range(1, 231):
        func_name = f'stem_volume_formula_{formula_no}'
        f = getattr(stem_volumes.formulas, func_name)
        params = tuple(signature(f).parameters)
        param_units = tuple(extract_parameter_units(f))
        vol_unit = extract_volume_unit(f)

        all_formulas[func_name] = (f, params, param_units, vol_unit)

    # Step 2: Build genus-to-formula mapping using genus_species_common_dict
    genus_formula_names = {}
    for genus, info in genus_species_common_dict.items():
        formula_names = []
        for formula in info.get('formulas', []):
            if not formula:
                continue
            for formula_no in range(1, 231):
                func_name = f'stem_volume_formula_{formula_no}'
                if func_name in all_formulas:
                    f = all_formulas[func_name][0]
                    doc = getattr(f, '__doc__', '')
                    # DEBUG: print matching attempts
                    # print(f"Checking {func_name}: doc='{doc}' formula='{formula}'")
                    if formula.lower() in func_name.lower() or \
                       (doc and formula.lower() in doc.lower()):
                        formula_names.append(func_name)
        genus_formula_names[genus] = set(formula_names)

    # Step 3: Pre-fill all 230 columns with pd.NA
    formula_columns = [f'{name} [m3]' for name in all_formulas]
    empty_formulas_df = pd.DataFrame(pd.NA, index=result_df.index, columns=formula_columns)
    result_df = pd.concat([result_df, empty_formulas_df], axis=1)

    # Step 4: Group by genus and apply only relevant formulas
    genus_to_indices = get_genus_row_map(result_df['genus'])

    for genus, relevant_funcs in genus_formula_names.items():
        idxs = genus_to_indices.get(genus, [])
        if len(idxs) == 0:
            continue

        diameters = result_df.loc[idxs, 'diameter at breast height [mm]'].values
        heights = result_df.loc[idxs, 'height [dm]'].values

        for func_name in relevant_funcs:
            if func_name not in all_formulas:
                continue
            f, params, param_units, vol_unit = all_formulas[func_name]
            col_name = f'{func_name} [m3]'
            apply_func = partial(_apply_formula_cached, f, params, param_units, vol_unit)

            # Handle formulas with one or two parameters
            if len(params) == 1:
                # Only one parameter required (assume diameter)
                valid_mask = ~pd.isna(diameters)
                if not np.any(valid_mask):
                    continue
                valid_idxs = np.array(idxs)[valid_mask]
                valid_diameters = diameters[valid_mask]
                vectorized_func = np.vectorize(apply_func, otypes=[object])
                result = vectorized_func(valid_diameters, [pd.NA]*len(valid_diameters))
                result_df.loc[valid_idxs, col_name] = result
            else:
                # Two parameters required
                valid_mask = (~pd.isna(diameters)) & (~pd.isna(heights))
                if not np.any(valid_mask):
                    continue
                valid_idxs = np.array(idxs)[valid_mask]
                valid_diameters = diameters[valid_mask]
                valid_heights = heights[valid_mask]
                vectorized_func = np.vectorize(apply_func, otypes=[object])
                result = vectorized_func(valid_diameters, valid_heights)
                result_df.loc[valid_idxs, col_name] = result

    return result_df



if __name__ == '__main__':
    main()