import argparse
import os
import sys

def main():
    args = parse_arguments()

    if os.path.exists(args.output_file):
        print(f"Error: {args.output_file} already exists.", file=sys.stderr)
        print(f"This script won't overwrite it to avoid accidental data loss.", file=sys.stderr)
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Calculate stem volumes for given CSV file"
    )

    parser.add_argument("csv_file", help="Path to CSV file, e.g., path/to/test.csv.")
    parser.add_argument("output_file", help="Path to CSV file to save the added results in.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
