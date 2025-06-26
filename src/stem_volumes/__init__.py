"""This module implements a command to apply the stem volume to a CSV file."""

import argparse
import cProfile
import os
import pstats
import re
import sys
import time
from inspect import signature

import numpy as np
import pandas as pd
from line_profiler import LineProfiler

import stem_volumes.formulas
from stem_volumes.genus_dict import genus_species_common_dict
from stem_volumes.utils import (
    clean_data,
    convert_volume_to_m3,
    extract_parameter_units,
    extract_volume_unit,
    match_species_names,
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


def calculate_stem_volumes(df):
    """Calculates the stem volumes for the given DataFrame."""
    df = df.copy()
    df['genus_species'] = match_species_names(df)

    all_formulas = {}
    for formula_no in range(1, 231):
        func_name = f'stem_volume_formula_{formula_no}'
        f = getattr(stem_volumes.formulas, func_name)
        params = tuple(signature(f).parameters)
        param_units = tuple(extract_parameter_units(f))
        vol_unit = extract_volume_unit(f)
        docstring = f.__doc__ or ''
        match = re.search(r'Species:\s*([^\n\(]+)', docstring)
        sci_name = match.group(1).strip() if match else ''
        all_formulas[func_name] = (f, params, param_units, vol_unit, sci_name)

    formula_columns = [f'{name} [m3]' for name in all_formulas]
    # Create a DataFrame with all new columns initialized to pd.NA
    new_cols_df = pd.DataFrame(
        {col: pd.NA for col in formula_columns}, index=df.index
    )

    # Concatenate the new columns with the original DataFrame
    df = pd.concat([df, new_cols_df], axis=1)

    # de-fragment DataFrame to improve performance
    # df = df.copy()

    unit_conversion_factors = {'mm': 0.001, 'cm': 0.01, 'dm': 0.1, 'm': 1}
    input_units = {'D': 'mm', 'H': 'dm'}
    diameter_raw = df['diameter at breast height [mm]'].to_numpy()
    height_raw = df['height [dm]'].to_numpy()

    allowed_formula_map = df['genus_species'].apply(
        lambda gs: set(
            genus_species_common_dict.get(gs[0], {}).get('formulas', [])
        )
        if gs
        else set()
    )

    for func_name, (
        f,
        params,
        param_units,
        vol_unit,
        sci_name,
    ) in all_formulas.items():
        mask = allowed_formula_map.apply(
            lambda formulas: sci_name in formulas
        ).to_numpy()
        if not np.any(mask):
            continue

        values = np.full(df.shape[0], pd.NA, dtype='object')
        try:
            if len(params) == 2:
                d_conv = (
                    unit_conversion_factors[input_units[params[0]]]
                    / unit_conversion_factors[param_units[0]]
                )
                h_conv = (
                    unit_conversion_factors[input_units[params[1]]]
                    / unit_conversion_factors[param_units[1]]
                )
                d_converted = diameter_raw * d_conv
                h_converted = height_raw * h_conv
                values[mask] = f(d_converted[mask], h_converted[mask])
            elif len(params) == 1:
                d_conv = (
                    unit_conversion_factors[input_units[params[0]]]
                    / unit_conversion_factors[param_units[0]]
                )
                d_converted = diameter_raw * d_conv
                values[mask] = f(d_converted[mask])
        except Exception:
            for i in np.where(mask)[0]:
                try:
                    if len(params) == 2:
                        values[i] = f(d_converted[i], h_converted[i])
                    elif len(params) == 1:
                        values[i] = f(d_converted[i])
                except Exception:
                    values[i] = pd.NA

        values = [
            convert_volume_to_m3(v, vol_unit) if pd.notna(v) else pd.NA
            for v in values
        ]
        df[f'{func_name} [m3]'] = values

    return df.drop(columns=['genus_species'])


if __name__ == '__main__':
    main()
