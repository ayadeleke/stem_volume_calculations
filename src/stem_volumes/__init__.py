"""This module implements a command to apply the stem volume to a CSV file."""

import argparse
import cProfile
import os
import pstats
import sys
import time
from functools import lru_cache
from inspect import signature

import numpy as np
import pandas as pd
from line_profiler import LineProfiler

import stem_volumes.formulas
from stem_volumes.species_to_formula_map import species_to_formulas
from stem_volumes.utils import (
    clean_data,
    convert_volume_to_m3,
    extract_parameter_units,
    extract_volume_unit,
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
    """Parses command-line arguments for the script.

    Returns:
        Namespace: An argparse.Namespace object containing the parsed arguments:
            - csv_file (str): Path to the input CSV file.
            - output_file (str): Path to the output CSV file where results will be saved.
    """
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


@lru_cache(maxsize=None)
def get_formula_metadata(formula_no: int):
    """Returns metadata about a stem volume formula by its number.

    Args:
        formula_no: The number of the stem volume formula.

    Returns:
        A tuple containing:
            - The name of the stem volume formula function.
            - The stem volume formula function itself.
            - A tuple of the parameter names.
            - A tuple of the parameter units.
            - The unit of the stem volume returned by the formula.
    """
    func_name = f'stem_volume_formula_{formula_no}'
    func = getattr(stem_volumes.formulas, func_name)
    params = tuple(signature(func).parameters)
    param_units = tuple(extract_parameter_units(func))
    vol_unit = extract_volume_unit(func)
    return func_name, func, params, param_units, vol_unit


@lru_cache(maxsize=None)
def get_conversion_factor(from_unit: str, to_unit: str) -> float:
    """Returns the conversion factor to convert a measurement from one unit to another.

    Args:
        from_unit: The unit of the original measurement ('mm', 'cm', 'dm', 'm').
        to_unit: The unit to convert the measurement to ('mm', 'cm', 'dm', 'm').

    Returns:
        The conversion factor to apply to the original measurement.
    """
    unit_conversion_factors = {'mm': 0.001, 'cm': 0.01, 'dm': 0.1, 'm': 1}
    return unit_conversion_factors[from_unit] / unit_conversion_factors[to_unit]


@lru_cache(maxsize=None)
def _apply_formula_cached(
    func_name, d, h, param1_unit, param2_unit, vol_unit, param_names
):
    """Apply formula with cached unit conversions and safe fallback."""
    try:
        func = getattr(stem_volumes.formulas, func_name)
        args = []
        # Convert diameter if used
        if 'D' in param_names:
            d_conv = get_conversion_factor('mm', param1_unit)
            args.append(d * d_conv)
        # Convert height if used
        if 'H' in param_names and h is not None:
            h_conv = get_conversion_factor('dm', param2_unit)
            args.append(h * h_conv)
        volume = func(*args)
        return convert_volume_to_m3(volume, vol_unit)
    except Exception:
        return pd.NA


# Precompute all formula metadata at import time
ALL_FORMULAS = {
    f'stem_volume_formula_{formula_no}': get_formula_metadata(formula_no)[2:]
    for formula_no in range(1, 231)
}


def calculate_stem_volumes(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate stem volumes for given trees in a CSV file.

    Parameters:
        df: A DataFrame containing the following columns
            - species: The species of the tree (string)
            - diameter at breast height [mm]: The diameter of the tree at breast height (float)
            - height [dm]: The height of the tree (float)

    Returns:
        A DataFrame with the same columns as the input, plus the calculated stem volumes
        for each tree, with column names ending in "[m3]"
    """
    df = df.copy()

    # Use precomputed metadata
    all_formulas = ALL_FORMULAS
    formula_names = list(all_formulas.keys())

    # Precompute allowed formulas as a DataFrame (rows: trees, cols: formulas)
    allowed_sets = df['species'].apply(
        lambda sp: set(species_to_formulas.get(sp.lower(), []))
        if isinstance(sp, str)
        else set()
    )
    allowed_mask = pd.DataFrame(
        [[fn in allowed for fn in formula_names] for allowed in allowed_sets],
        columns=formula_names,
        index=df.index,
    )

    # Prepare results DataFrame
    results = pd.DataFrame(
        pd.NA, index=df.index, columns=[f'{fn} [m3]' for fn in formula_names]
    )

    diameter_raw = df['diameter at breast height [mm]'].to_numpy()
    height_raw = df['height [dm]'].to_numpy()

    for j, func_name in enumerate(formula_names):
        params, param_units, vol_unit = all_formulas[func_name]
        mask = allowed_mask[func_name].to_numpy()
        if not np.any(mask):
            continue

        # Only compute for rows where mask is True
        idx = np.where(mask)[0]
        vals = []
        for i in idx:
            d = diameter_raw[i]
            h = height_raw[i] if len(params) > 1 else None
            val = _apply_formula_cached(
                func_name,
                d,
                h,
                param_units[0],
                param_units[1] if len(params) > 1 else None,
                vol_unit,
                params,
            )
            vals.append(val)
        results.iloc[idx, j] = vals

    return pd.concat([df, results], axis=1)


if __name__ == '__main__':
    main()
