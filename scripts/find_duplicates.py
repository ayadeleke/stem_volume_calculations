import pandas as pd

# Path to your CSV file
csv_path = "data/inputs/trees.csv"

# Read the CSV file
df = pd.read_csv(csv_path)

# Count rows before and after dropping duplicates
before = len(df)
after = len(df.drop_duplicates())
dropped = before - after

print(f"Rows before drop_duplicates: {before}")
print(f"Rows after drop_duplicates: {after}")
print(f"Number of dropped duplicates: {dropped}")

# Add index as a column for grouping
df_with_index = df.copy()
df_with_index['__index__'] = df_with_index.index

# Find all duplicate rows and collect their indices
dup_indices = (
    df_with_index[df_with_index.duplicated(subset=list(df.columns), keep=False)]
    .groupby(list(df.columns))
    .agg({'__index__': lambda idxs: list(idxs)})
    .rename(columns={'__index__': 'indices'})
    .reset_index()
)

# Count occurrences
dup_indices['count'] = dup_indices['indices'].apply(len)

# Only keep rows that are true duplicates (appear more than once)
dup_indices = dup_indices[dup_indices['count'] > 1]
dup_indices = dup_indices.sort_values('count', ascending=False)

if dup_indices.empty:
    print("No duplicate rows found.")
else:
    print("Duplicate rows (count > 1) and their indices:")
    print(dup_indices)
    # Save to CSV
    dup_indices.to_csv("duplicates_with_counts_and_indices.csv", index=False)
    print(f"\nSaved duplicate rows with indices to 'duplicates_with_counts_and_indices.csv'")
    # Number of dropped duplicates (all but one in each group)
    dropped = int((dup_indices['count'] - 1).sum())
    print(f"Total duplicate rows: {int(dup_indices['count'].sum())}")
    print(f"Number of dropped duplicates (would be removed by drop_duplicates): {dropped}")

# Actual dropped duplicates
dropped_rows = df[df.duplicated(keep='first')]
print(f"Number of dropped duplicates (actual rows dropped): {len(dropped_rows)}")
dropped_rows.to_csv("dropped_duplicates.csv", index=False)

# Run this script with:
# uv run python scripts/find_duplicates.py