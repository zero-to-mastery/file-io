import pandas as pd

spotify_data = pd.read_csv('spotify-2023.csv')

# Number of songs in the file
print(f'Total number of songs in this file: {len(spotify_data)}')

# Number of songs in the key of E
total_e_key_songs = spotify_data[spotify_data['key'] == 'E']
print(f'Total number of songs in the key of E: {len(total_e_key_songs)}')

# Year with most number of songs
song_count_in_a_year = spotify_data['released_year'].value_counts()
year_with_most_songs = song_count_in_a_year.idxmax()
print(f'{year_with_most_songs} is the year with most number of songs. Total number of songs in this year: {song_count_in_a_year[year_with_most_songs]}')