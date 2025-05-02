"""This module implements a command to apply the stem volume to a CSV file."""

import argparse
import cProfile
import os
import pstats
import sys
import time
from inspect import signature

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


def calculate_stem_volumes(df):
    """Applies the stem volume formulas to the given data frame.

    Args:
        df: Data frame to perform the calculations on.

    Returns:
        the modified data frame
    """
    # add colums for formulas to fill
    df_empty_volumes = pd.DataFrame(
        {f'volume formula {i} [m3]': pd.NA for i in range(1, 231)},
        index=df.index,
    )
    df = pd.concat([df, df_empty_volumes], axis=1)

    # iterate over rows to calculate each volume per formula and add the value
    # to the dataframe
    # FIXME
    # this is sooo slow
    for idx, row in df.iterrows():
        for formula_no in range(1, 231):
            function_name = f'stem_volume_formula_{formula_no}'
            f = getattr(formulas, function_name)
            params = list(signature(f).parameters)
            parameter_units = extract_parameter_units(f)

            # convert units to what the formula expects
            UNITS = {
                'D': ['mm', 'cm', 'dm', 'm'],  # units for diameters
                'H': ['dm', 'm'],  # units for heights
            }
            diameter_mm = row['diameter at breast height [mm]']
            height_dm = row['height [dm]']
            args = {'D': diameter_mm, 'H': height_dm}
            converted_args = [
                args[par_name] / 10 ** UNITS[par_name].index(parameter_units[i])
                for i, par_name in enumerate(params)
            ]

            # apply formula and convert to m3
            # FIXME
            # this bindly applies the formula even if it not a good fit
            volume = f(*converted_args)
            volume_unit = extract_volume_unit(f)
            volume = convert_volume_to_m3(volume, volume_unit)
            column_name = f'volume formula {formula_no} [m3]'
            df.loc[idx, column_name] = volume

    return df


if __name__ == '__main__':
    main()
