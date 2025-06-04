"""This module implements a command to apply the stem volume to a CSV file."""
import argparse
import cProfile
import os
import pstats
import re
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
from stem_volumes.genus_dict import genus_species_common_dict
from stem_volumes.utils import (
    convert_volume_to_m3,
    extract_parameter_units,
    extract_volume_unit,
    clean_data,
    match_species_names,
    match_genus_to_functions,
    get_genus_row_map
)


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

    # Drop 'genus_species' before saving
    if 'genus_species' in df_calculated.columns:
        df_calculated = df_calculated.drop(columns=['genus_species'])
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


def _process_formula_batch(formula_data, diameters, heights):
    """Process a batch of formulas for all rows using vectorized operations where possible."""
    results = {}

    diameters_np = np.array(diameters)
    heights_np = np.array(heights)

    for formula_no, (f, params, parameter_units, volume_unit) in formula_data:
        column_name = f'volume formula {formula_no} [m3]'
        apply_func = partial(_apply_formula_cached, f, params, parameter_units, volume_unit)

        values = []
        for d, h in zip(diameters_np, heights_np):
            try:
                # Ensure that pd.NA doesn't propagate to apply_func
                d_val = None if pd.isna(d) else d
                h_val = None if pd.isna(h) else h
                values.append(apply_func(d_val, h_val))
            except Exception:
                values.append(pd.NA)

        results[column_name] = values

    return results

def calculate_stem_volumes(df):
    """Applies only matching stem volume formulas to each row."""
    result_df = df.copy()
    # This now returns a list of (genus, species) tuples
    result_df['genus_species'] = match_species_names(result_df)

    # Prepare all formulas
    all_formulas = {}
    for formula_no in range(1, 231):
        func_name = f'stem_volume_formula_{formula_no}'
        f = getattr(stem_volumes.formulas, func_name)
        params = tuple(signature(f).parameters)
        param_units = tuple(extract_parameter_units(f))
        vol_unit = extract_volume_unit(f)
        docstring = f.__doc__ or ""
        # Extract scientific species name from docstring
        match = re.search(r"Species:\s*([^\n\(]+)", docstring)
        sci_name = match.group(1).strip() if match else ""
        all_formulas[func_name] = (f, params, param_units, vol_unit, sci_name)

    # Pre-fill all 230 columns with pd.NA
    formula_columns = [f'{name} [m3]' for name in all_formulas]
    empty_formulas_df = pd.DataFrame(pd.NA, index=result_df.index, columns=formula_columns)
    result_df = pd.concat([result_df, empty_formulas_df], axis=1)

    # Apply only matching formulas row-wise
    for idx, row in result_df.iterrows():
        genus, _ = row['genus_species']
        if genus is None:
            continue
        allowed_formulas = set(genus_species_common_dict[genus]["formulas"])
        diameter = row['diameter at breast height [mm]']
        height = row['height [dm]']
        for func_name, (f, params, param_units, vol_unit, sci_name) in all_formulas.items():
            # Only apply if the formula's species matches allowed scientific names
            if sci_name in allowed_formulas:
                apply_func = partial(_apply_formula_cached, f, params, param_units, vol_unit)
                value = apply_func(diameter, height)
                result_df.at[idx, f"{func_name} [m3]"] = value

    return result_df



if __name__ == '__main__':
    main()
