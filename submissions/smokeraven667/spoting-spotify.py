import os
import csv
from collections import Counter

artist_name_index = 1
filename = "spotify-2023.csv"
path = os.getcwd()
songs = None

# READ FILE
csv_file_path = os.path.join(path, filename)
with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    songs = list(csv_reader)

# # PROCESS FILE DATA
counter_artist = Counter()
counter_key = Counter()
for song in songs:
    counter_artist[song['artist(s)_name']] += 1
    counter_key[song['key']] += 1
most_common_artist = Counter(counter_artist).most_common(1)
most_common_key = Counter(counter_key).most_common(1)

# # REPORT DATA
print(f'Number of songs: {len(songs)}')
print(f'Number of artists: {len(set([x["artist(s)_name"] for x in songs]))}')
print(
    f'Most common artist: {most_common_artist[0][0]} with {most_common_artist[0][1]} songs.')
print(
    f'Most common key: {most_common_key[0][1]} songs in the key of {most_common_key[0][0]}.')
