import pandas as pd
from collections import Counter

def count_songs_with_key(data, key):
    counts = data['key'].value_counts().get(key, 0)
    return counts

def count_occurrences_of_values(data):
    artist_names = data['artist(s)_name'].str.split(', ')
    all_artists = [artist for sublist in artist_names for artist in sublist]
    count_artists = Counter(all_artists)
    most_common_artist = count_artists.most_common(1)[0][0]
    return most_common_artist

# Read the CSV file
results = pd.read_csv('spotify-2023.csv')

# Solution 1: Number of songs
num_of_songs = len(results)
print("Number of songs:", num_of_songs)

# Solution 2: Number of songs with key E
num_of_songs_with_E = count_songs_with_key(results, 'E')
print("Number of songs with key E:", num_of_songs_with_E)

# Solution 3: Most streamed artist
most_occurrences = count_occurrences_of_values(results)
print("Most streamed artist:", most_occurrences)
