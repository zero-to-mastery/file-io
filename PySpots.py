import pandas as pd

def count_songs_with_key(data):
    # Count the number of songs with the key 'E'
    return data['key'].value_counts().get('E', 0)

def count_occurrences_of_values(data):
    # Count the occurrences of artists in the dataset
    artists = data['artist(s)_name'].str.split(', ')
    artist_counts = {}
    
    for artist_list in artists:
        for artist in artist_list:
            artist = artist.strip()
            artist_counts[artist] = artist_counts.get(artist, 0) + 1
    
    # Find the artist with the most occurrences
    most_occurrences = max(artist_counts, key=artist_counts.get)
    
    return most_occurrences

if __name__ == '__main':
    # Read the CSV file
    results = pd.read_csv('spotify-2023.csv')

    # Solution 1: Number of songs
    num_of_songs = len(results)
    print("Number of songs:", num_of_songs)

    # Solution 2: Number of songs with key 'E'
    num_of_songs_with_E = count_songs_with_key(results)
    print("Number of songs with key E:", num_of_songs_with_E)

    # Solution 3: Most streamed artist
    most_streamed_artist = count_occurrences_of_values(results)
    print("Most streamed artist:", most_streamed_artist)
