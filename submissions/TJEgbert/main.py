"""Project file-io from zero-to-Mastery
"""

import pandas as pd

def load_csv():
    """Loads the spotify-2023.csv file

    Returns:
        DataFrame: Pandas DataFrame containing the csv data
    """
    return pd.read_csv('spotify-2023.csv', encoding='latin-1')


def number_of_songs(data):
    """Gets the number of rows from the DataFrame

    Args:
        data (DataFrame): Pandas DataFrame

    Returns:
        int: The number of rows in the DataFrame
    """
    return data.shape[0]

def number_of_songs_in_E(data):
    """Gets the number songs that are in the key of E

    Args:
        data (DataFrame): Pandas DataFrame

    Returns:
        int: The number of songs
    """
    return data[data.key == 'E'].shape[0]

def values_in_columns(data, column):
    """Gets the most frequently data from a column

    Args:
        data (DataFrame): Pandas DataFrame
        column (string): The name of the column the user wants to access

    Returns:
        string: The most frequent data from the column
    """
    df = data[column].value_counts().index.tolist()
    return df[0]

def main():
    """Driven Function
    """
    data_df = load_csv()
    print(f'There are {number_of_songs(data_df)} in the csv file')
    print(f'The number of songs in E is {number_of_songs_in_E(data_df)}')
    artist = values_in_columns(data_df, 'artist(s)_name')
    print(f'The most common artist is {artist}')


if __name__ == "__main__":
    main()