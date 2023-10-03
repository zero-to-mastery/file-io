import csv
from collections import Counter

try:
    # Open the CSV file
    with open('submissions/thugbunnys/spotify-2023.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# Calculate the number of songs
num_songs = len(data)
print(f"Number of songs: {num_songs}")

# Calculate the number of songs in the key of E
num_songs_in_e = sum(1 for row in data if row['key'] == 'E')
print(f"Number of songs in the key of E: {num_songs_in_e}")

# Calculate the most common artist
counter = Counter(row['artist(s)_name'] for row in data)
most_common_artist = counter.most_common(1)[0]
print(f"Most common artist: {most_common_artist[0]} with {most_common_artist[1]} songs")