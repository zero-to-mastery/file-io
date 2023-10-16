import csv

# Open the CSV file and store the data in a list of dictionaries
with open('spotify-2023.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Number of Songs in the File
num_songs = len(data)

# Number of Songs in the Key of E
songs_in_e = len([row for row in data if row['key'] == 'E'])

# Occurrences of Artist Names and Value
artist_counts = {}
most_common_artist = None
artist_count = 0

for row in data:
    artist = row['artist(s)_name']
    artist_counts[artist] = artist_counts.get(artist, 0) + 1
    if artist_counts[artist] > artist_count:
        most_common_artist = artist
        artist_count = artist_counts[artist]
    
print(f'Number of songs: {num_songs}')
print(f'Number of songs in the key of E: {songs_in_e}')
print(f'Most common artist: {most_common_artist}, occurs {artist_count} times')