import csv
from collections import Counter

# Define the filename for the Spotify CSV data
filename = 'spotify-2023.csv'

# Read and analyze the CSV file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Extract the header fields from the file
    header = next(csvreader)

    # Initialize data containers
    data_rows = []  # Store all data rows
    artist_names = []  # Store artist names for analysis

    # Iterate through the CSV data
    for row in csvreader:
        data_rows.append(row)

        # Extract and record artist names
        artist_name = row[header.index('artist(s)_name')]
        artist_names.append(artist_name)

    # Count the number of songs in the key of 'E'
    songs_in_key_E = sum(1 for row in data_rows if row[header.index('key')] == 'E')

    # Determine the most frequently occurring artist name
    most_common_artist_name = max(Counter(artist_names).keys(), key=lambda k: Counter(artist_names)[k])

# Output the results
print(f'Total number of songs in the file: {len(data_rows)}')
print(f'Number of songs in the key of E: {songs_in_key_E}')
print(f'Most common artist name: {most_common_artist_name}')
