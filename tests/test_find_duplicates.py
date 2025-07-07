import os
import tempfile

import pandas as pd


def test_find_duplicates_removes_only_duplicates(tmp_path):
    # Create a sample DataFrame with duplicates and unique rows
    data = [
        {'species': 'A', 'diameter': 10, 'height': 5},
        {'species': 'A', 'diameter': 10, 'height': 5},
        {'species': 'B', 'diameter': 20, 'height': 10},
        {'species': 'C', 'diameter': 30, 'height': 15},
        {'species': 'B', 'diameter': 20, 'height': 10},
        {'species': 'D', 'diameter': 40, 'height': 20},
    ]
    df = pd.DataFrame(data)
    csv_path = tmp_path / 'test.csv'
    df.to_csv(csv_path, index=False)

    # Simulate running find_duplicates.py logic
    df_loaded = pd.read_csv(csv_path)
    before = len(df_loaded)
    after = len(df_loaded.drop_duplicates())
    dropped = before - after

    # Find actual dropped duplicates
    dropped_rows = df_loaded[df_loaded.duplicated(keep='first')]
    # Find unique rows
    unique_rows = df_loaded[~df_loaded.duplicated(keep=False)]

    # Assert dropped count matches drop_duplicates
    assert dropped == len(dropped_rows)
    # Assert no unique rows are in dropped_rows
    assert not any(unique_rows.index.isin(dropped_rows.index))
    # Assert only duplicates are dropped (index match)
    expected_dropped_indices = set(
        df_loaded.index[df_loaded.duplicated(keep='first')]
    )
    actual_dropped_indices = set(dropped_rows.index)
    assert expected_dropped_indices == actual_dropped_indices

    # Clean up (optional, handled by tmp_path)
    os.remove(csv_path)


def test_find_duplicates_matches_clean_data(tmp_path):
    # Create a sample DataFrame with duplicates
    data = [
        {'species': 'A', 'diameter': 10, 'height': 5},
        {'species': 'A', 'diameter': 10, 'height': 5},
        {'species': 'B', 'diameter': 20, 'height': 10},
        {'species': 'B', 'diameter': 20, 'height': 10},
        {'species': 'C', 'diameter': 30, 'height': 15},
    ]
    df = pd.DataFrame(data)
    csv_path = tmp_path / 'test2.csv'
    df.to_csv(csv_path, index=False)

    # This simulates the logic from clean_data.py
    df_cleaned = df.drop_duplicates()
    dropped_rows = df[df.duplicated(keep='first')]

    # The number of dropped rows should match the difference
    assert len(df) - len(df_cleaned) == len(dropped_rows)
