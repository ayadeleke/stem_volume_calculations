"""This script reads a Feather file and writes it to a CSV file."""

import pandas as pd

# Input and output file paths
feather_file = 'data/volume_calculated.feather'
csv_file = 'data/volume_calculated.csv'

# Read Feather file
df = pd.read_feather(feather_file)

# Write to CSV
df.to_csv(csv_file, index=False)
print(f"Converted '{feather_file}' to '{csv_file}'")
