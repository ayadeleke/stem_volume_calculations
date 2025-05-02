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
from line_profiler import LineProfiler

import stem_volumes.formulas
from stem_volumes.utils import (
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

    df_calculated = calculate_stem_volumes(df)
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
    """Applies the stem volume formulas to the given data frame."""
    result_df = df.copy()
    diameters = df['diameter at breast height [mm]'].values
    heights = df['height [dm]'].values

    formula_metadata = []
    for formula_no in range(1, 231):
        function_name = f'stem_volume_formula_{formula_no}'
        f = getattr(formulas, function_name)
        params = tuple(signature(f).parameters)
        parameter_units = tuple(extract_parameter_units(f))  # convert to tuple
        volume_unit = extract_volume_unit(f)
        formula_metadata.append((formula_no, (f, params, parameter_units, volume_unit)))

    num_workers = min(os.cpu_count() or 4, 8)
    batch_size = max(1, len(formula_metadata) // num_workers)
    formula_batches = [formula_metadata[i:i + batch_size] for i in range(0, len(formula_metadata), batch_size)]

    all_results = {}
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        future_to_batch = {
            executor.submit(_process_formula_batch, batch, diameters, heights): i
            for i, batch in enumerate(formula_batches)
        }

        for future in as_completed(future_to_batch):
            batch_results = future.result()
            all_results.update(batch_results)

    result_df = pd.concat([result_df, pd.DataFrame(all_results)], axis=1)


    return result_df


if __name__ == '__main__':
    main()
