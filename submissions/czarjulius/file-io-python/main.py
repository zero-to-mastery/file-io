import os
import csv
from collections import defaultdict

def spotify_data_analyzer(csv_file_path, options={}):
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")

    song_count = 0
    key_e_song_count = 0
    value_counts = defaultdict(int)

    key = options.get('key', 'E')
    column_to_count = options.get('columnToCount', 'artist(s)_name')

    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song_count += 1

            if key and row.get('key', '').upper() == key.upper():
                key_e_song_count += 1

            column_value = row.get(column_to_count, '')
            if column_value:
                normalized_value = column_value.lower()
                value_counts[normalized_value] += 1

    most_common_value = ''
    highest_count = 0
    for value, count in value_counts.items():
        if count > highest_count:
            most_common_value = value
            highest_count = count

    result = {
        'totalSongs': song_count,
        'keyESongs': key_e_song_count,
        'mostCommonValue': most_common_value,
        'highestCount': highest_count,
    }
    return result

csv_file_path = os.path.join(os.path.dirname(__file__), '../spotify-2023.csv')

options = {
    'key': 'E',
    'columnToCount': 'artist(s)_name',
}

try:
    result = spotify_data_analyzer(csv_file_path, options)
    print(f"Total number of songs in the CSV file: {result['totalSongs']}")
    print(f"Total number of songs in the key of E: {result['keyESongs']}")
    print(f"Most common value in the 'artist(s)_name' column: {result['mostCommonValue']} ({result['highestCount']} occurrences)")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print("Something went wrong:", e)
