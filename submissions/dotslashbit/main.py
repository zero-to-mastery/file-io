import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv('spotify-2023.csv', encoding='latin1')

# Task 1: Number of songs in the file
num_songs = len(df)


# Task 2: Number of songs in the key of E
num_songs_in_key_e = len(df[df['key'] == 'E'])  

# Task 3: Count occurrences of artist name(s) and determine the most common value
artist_counts = df['artist(s)_name'].value_counts()
most_common_artist = artist_counts.idxmax()
most_common_artist_count = artist_counts.max()

# Outputs
print(f'Total number of songs in the file: {num_songs}')
print(f'Number of songs in the key of E: {num_songs_in_key_e}')
print(f'Most common artist: {most_common_artist}, Occurrences: {most_common_artist_count}')
