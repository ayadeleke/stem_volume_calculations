import pandas as pd
import sys

def clean_data(file_path: str) -> pd.DataFrame:
    """Load and clean the dataset.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Load the dataset
    df = pd.read_csv(file_path,  index_col=0)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    df.fillna(method='ffill', inplace=True)

    # Capitalize species column
    df['species'] = df['species'].str.capitalize()

    return df



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_data.py <file_path>")
    else:
        file_path = sys.argv[1]
        cleaned_df = clean_data(file_path)
        print(cleaned_df.head())  # print first few rows as example
