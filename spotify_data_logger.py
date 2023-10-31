import csv
import os

# Load Spotify data from the CSV file
def load_data(filename):
    with open(filename, mode='r', encoding='latin1') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Challenge 1: Identify the number of songs in the file
def total_songs(data):
    return len(data)

# Challenge 2: Identify the number of songs in the key of E
def songs_in_key_e(data):
    count = 0
    for row in data:
        if row['key'] == 'E':
            count += 1
    return count

# Challenge 3: Count the occurrences of values in a specified column (artist names)
def most_common_artist(data):
    artist_count = {}
    for row in data:
        artist = row['artist(s)_name']
        if artist in artist_count:
            artist_count[artist] += 1
        else:
            artist_count[artist] = 1
    return max(artist_count, key=artist_count.get)

if __name__ == "__main__":
    # Create a folder for your project with your github handle
    folder_name = "your_github_handle"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Load data
    data = load_data('spotify-2023.csv')

    # Perform challenges
    print(f"Total number of songs: {total_songs(data)}")
    print(f"Number of songs in the key of E: {songs_in_key_e(data)}")
    print(f"The most common artist is: {most_common_artist(data)}")
