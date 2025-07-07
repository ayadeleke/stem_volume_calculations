"""This module implements a command to apply the stem volume to a CSV file."""

import argparse
import cProfile
import os
import pstats
import sys
import time
from concurrent.futures import ProcessPoolExecutor
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

    df_calculated.to_feather(args.output_file.replace('.csv', '.feather'))
    toc = time.perf_counter()
    print(f'Writing the file took {toc - tic:.6f} seconds')

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
    func_name,
    *,
    d=None,
    h=None,
    param_unit_D=None,
    param_unit_H=None,
    vol_unit=None,
    params=(),
):
    """Apply formula with cached unit conversions and safe fallback."""
    try:
        func = getattr(stem_volumes.formulas, func_name)
        args = []

        # Convert diameter if used
        if 'D' in params and d is not None:
            d_conv = get_conversion_factor('mm', param_unit_D)
            args.append(d * d_conv)

        # Convert height if used
        if 'H' in params and h is not None:
            h_conv = get_conversion_factor('dm', param_unit_H)
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


def process_chunk(
    start, end, diameter, height, allowed_formula_lists, all_formulas
):
    """Process a chunk of input data in parallel.

    Args:
        start: The start index of the chunk in the original DataFrame.
        end: The end index of the chunk in the original DataFrame.
        diameter: The diameters of the trees in the chunk as a numpy array.
        height: The heights of the trees in the chunk as a numpy array.
        allowed_formula_lists: A list of allowed formula lists for each row in the chunk.
        all_formulas: A dictionary of all formula metadata.

    Returns:
        A pandas DataFrame containing the computed stem volumes for the given chunk.
    """
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
            row_result[f'{func_name} [m3]'] = val
        chunk_results.append(row_result)
    return pd.DataFrame(chunk_results, index=range(start, end))


# Precompute all formula metadata at import time
ALL_FORMULAS = {
    f'stem_volume_formula_{formula_no}': get_formula_metadata(formula_no)[2:]
    for formula_no in range(1, 231)
}

ROW_THRESHOLD = (
    1000  # Threshold for switching between row-wise and vectorized processing
)


def calculate_stem_volumes(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate stem volumes using row-wise or vectorized logic depending on dataset size."""
    if len(df) < ROW_THRESHOLD:
        return _calculate_stem_volumes_rowwise(df)
    else:
        return _calculate_stem_volumes_vectorized(df)


def _calculate_stem_volumes_rowwise(df: pd.DataFrame) -> pd.DataFrame:
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
            args = []
            if 'D' in params:
                args.append(diameter_raw[i])
            if 'H' in params:
                args.append(height_raw[i])
            param_unit_D = (
                param_units[params.index('D')] if 'D' in params else None
            )
            param_unit_H = (
                param_units[params.index('H')] if 'H' in params else None
            )

            val = _apply_formula_cached(
                func_name,
                d=diameter_raw[i] if 'D' in params else None,
                h=height_raw[i] if 'H' in params else None,
                param_unit_D=param_unit_D,
                param_unit_H=param_unit_H,
                vol_unit=vol_unit,
                params=params,
            )

            vals.append(val)
        results.iloc[idx, j] = vals

    return pd.concat([df, results], axis=1)


def _calculate_stem_volumes_vectorized(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate stem volumes for a given DataFrame using formulas from a publication.

    Args:
        df (pd.DataFrame): Input DataFrame containing the following columns:
            - diameter at breast height [mm]
            - height [dm]
            - species

    Returns:
        pd.DataFrame: Input DataFrame with additional columns for each
            species-specific formula, containing the computed stem volumes in m3.
    """
    df = df.copy()
    diameter_col = 'diameter at breast height [mm]'
    height_col = 'height [dm]'
    species_col = 'species'

    df[species_col] = df[species_col].str.lower().fillna('')

    volume_results = {}

    for species_name, group_df in df.groupby(species_col):
        allowed_formulas = species_to_formulas.get(species_name, [])
        if not allowed_formulas:
            continue

        d = group_df[diameter_col].to_numpy()
        h = group_df[height_col].to_numpy()

        for func_name in allowed_formulas:
            if func_name not in ALL_FORMULAS:
                continue
            params, param_units, vol_unit = ALL_FORMULAS[func_name]

            # Unit conversion (robust to parameter order)
            d_conv = (
                get_conversion_factor('mm', param_units[params.index('D')])
                if 'D' in params
                else None
            )
            h_conv = (
                get_conversion_factor('dm', param_units[params.index('H')])
                if 'H' in params
                else None
            )

            # Prepare arguments
            args = []
            if 'D' in params:
                args.append(d * d_conv)
            if 'H' in params:
                args.append(h * h_conv)

            func = getattr(stem_volumes.formulas, func_name)

            try:
                volumes = func(*args)  # NumPy-aware formula
                volumes_m3 = convert_volume_to_m3(volumes, vol_unit)
            except Exception:
                volumes_m3 = np.full(len(group_df), pd.NA)

            colname = f'{func_name} [m3]'
            if colname not in volume_results:
                volume_results[colname] = pd.Series(
                    index=df.index, dtype='object'
                )
            volume_results[colname].loc[group_df.index] = volumes_m3

    # Combine all new columns into a DataFrame and concatenate at once
    results_df = pd.DataFrame(volume_results)
    ordered_cols = [
        f'stem_volume_formula_{i} [m3]'
        for i in range(1, 231)
        if f'stem_volume_formula_{i} [m3]' in results_df.columns
    ]
    results_df = results_df[ordered_cols]

    df = pd.concat([df, results_df], axis=1)

    return df


if __name__ == '__main__':
    main()
