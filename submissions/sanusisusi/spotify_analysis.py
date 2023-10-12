import pandas as pd

def load_data(file_path):
    """
    Load Spotify data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None

def count_songs(data):
    """
    Identify the number of songs in the dataset.
    """
    if data is not None:
        num_songs = len(data)
        print(f"Number of songs in the dataset: {num_songs}")

def count_songs_in_key(data, key):
    """
    Identify the number of songs in a specific key.
    """
    if data is not None:
        key_songs = data[data['key'] == key]
        num_key_songs = len(key_songs)
        print(f"Number of songs in the key of {key}: {num_key_songs}")

def count_occurrences(data, column_name):
    """
    Count the occurrences of values in a specified column and determine the most common value.
    """
    if data is not None:
        occurrences = data[column_name].value_counts()
        most_common_value = occurrences.idxmax()
        print(f"Occurrences in the '{column_name}' column:")
        print(occurrences)
        print(f"\nThe most common value in '{column_name}': {most_common_value}")

if __name__ == "__main__":
    file_path = "spotify-2023.csv"
    
    # Load data
    spotify_data = load_data(file_path)

    # Task 1: Identify the number of songs
    count_songs(spotify_data)

    # Task 2: Identify the number of songs in the key of E
    count_songs_in_key(spotify_data, 'E')

    # Task 3: Count occurrences of artist names and determine the most common
    count_occurrences(spotify_data, 'artist_name')
