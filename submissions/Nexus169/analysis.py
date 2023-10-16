import csv


def load_file(filename):
    song_data = open(filename, encoding='UTF-8', mode='r')
    csv_reader = csv.DictReader(song_data, delimiter=',')
    return csv_reader


# Write a script to identify the number of songs in the file.
# Write a script that identify the number of songs in the key of E.
# Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

def count_songs(filename):
    song_count = 0
    with open(filename, encoding='UTF-8') as song_data:
        song_reader = csv.DictReader(song_data, delimiter=',')
        for song in song_reader:
            song_count += 1
    return song_count


def count_songs_with_key(filename, key_value):
    song_count = 0
    with open(filename, encoding='UTF-8') as song_data:
        song_reader = csv.DictReader(song_data, delimiter=',')
        for song in song_reader:
            if song['key'] == key_value:
                song_count += 1
    return song_count


def count_most_common_value(filename, column):
    count_cache = {}
    with open(filename, encoding='UTF-8') as song_data:
        song_reader = csv.DictReader(song_data, delimiter=',')
        for song in song_reader:
            if song[column] not in count_cache:
                count_cache[song[column]] = 1
            else:
                count_cache[song[column]] += 1
    most_common = max(count_cache, key=count_cache.get)
    return most_common

if __name__ == "__main__":
    filename = 'spotify-2023.csv'
    count = count_songs(filename)
    print(f'Total Songs: {count}')
    e_count = count_songs_with_key(filename, 'E')
    print(f'Songs in key of E: {e_count}')
    column = "artist(s)_name"
    most_common = count_most_common_value(filename, column)
    print(f'Most common {column}: {most_common}')


