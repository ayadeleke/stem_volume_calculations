"""This module implements a command to apply the stem volume to a CSV file."""

import argparse
import cProfile
import os
import pstats
import sys
import time
from functools import lru_cache
from inspect import signature
from concurrent.futures import ProcessPoolExecutor

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

def compute_volume_for_row(args):
    """Apply a stem volume formula to a single row of input data.

    The arguments given must be a tuple of the following:
        - The index of the row in the original DataFrame.
        - The name of the stem volume formula function to use.
        - The diameter of the tree in mm.
        - The height of the tree in dm.
        - The unit of the diameter in the formula.
        - The unit of the height in the formula.
        - The unit of the stem volume returned by the formula.
        - A tuple of the parameter names used by the formula.

    Returns a tuple of the index and the computed stem volume in m3.
    """
    i, func_name, d, h, param1_unit, param2_unit, vol_unit, param_names = args
    val = _apply_formula_cached(
        func_name, d, h, param1_unit, param2_unit, vol_unit, param_names
    )
    return i, val

def process_chunk(start, end, diameter, height, allowed_formula_lists, all_formulas):
    chunk_results = []
    for i in range(end - start):
        row_result = {}
        d = diameter[i]
        h = height[i]
        allowed = allowed_formula_lists[i]
        for func_name in allowed:
            if func_name not in all_formulas:
                continue
            params, param_units, vol_unit = all_formulas[func_name]
            val = _apply_formula_cached(
                func_name,
                d,
                h if len(params) > 1 else None,
                param_units[0],
                param_units[1] if len(params) > 1 else None,
                vol_unit,
                params,
            )
            row_result[f"{func_name} [m3]"] = val
        chunk_results.append(row_result)
    return pd.DataFrame(chunk_results, index=range(start, end))

def _process_chunk_wrapper(args):
    return process_chunk(*args)


# Precompute all formula metadata at import time
ALL_FORMULAS = {
    f'stem_volume_formula_{formula_no}': get_formula_metadata(formula_no)[2:]
    for formula_no in range(1, 231)
}


def calculate_stem_volumes(df: pd.DataFrame, num_workers: int = None) -> pd.DataFrame:
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

    diameter = df['diameter at breast height [mm]'].to_numpy()
    height = df['height [dm]'].to_numpy()
    species = df['species'].str.lower().fillna("").tolist()

    # Prepare allowed formulas per row
    allowed_formula_lists = [
        [f if f.startswith("stem_volume_formula_") else f"stem_volume_formula_{f}" for f in species_to_formulas.get(sp, [])]
        for sp in species
    ]

    # Split data into chunks
    chunk_size = 10_000
    indices = list(range(0, len(df), chunk_size))
    tasks = [
    (
        0,                          # start index in the sliced chunk
        end - start,               # end index in the sliced chunk
        diameter[start:end],       # sliced diameter
        height[start:end],         # sliced height
        allowed_formula_lists[start:end],  # sliced allowed formulas
        all_formulas
    )
    for start in indices
    for end in [min(start + chunk_size, len(df))]
]



    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        result_dfs = list(executor.map(_process_chunk_wrapper, tasks))


    results_df = pd.concat(result_dfs)
    results_df.index = df.index
    return pd.concat([df, results_df], axis=1)


if __name__ == '__main__':
    main()
