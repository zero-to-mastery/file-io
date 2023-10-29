import csv

def load_data(file):
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

spotify_data = load_data('spotify-2023.csv')

def count_songs(data):
    return len(data)

num_songs = count_songs(spotify_data)
print(f'The number of songs in the file is: {num_songs}')

def count_songs_in_key(data, key):
    songs_in_key = [song for song in data if song['key'] == key]
    return len(songs_in_key)

num_songs_in_key_E = count_songs_in_key(spotify_data, 'E')
print(f'The number of songs in the key of E is: {num_songs_in_key_E}')

def most_common_artist(data):
    artist_counts = {}
    for song in data:
        if song['artist'] in artist_counts:
            artist_counts[song['artist']] += 1
        else:
            artist_counts[song['artist']] = 1
    most_common_artist = max(artist_counts, key=artist_counts.get)
    return most_common_artist

print(f'The most common artist is: {most_common_artist(spotify_data)}')
