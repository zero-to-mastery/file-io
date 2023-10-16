def read_spotify_data():

    import pandas as pd

    data = pd.read_csv('spotify-2023.csv', encoding='utf-8')

    return data


def count_songs():
    """
    Challenge 1: Write a script to identify the number of songs in the file.
    """
    data = read_spotify_data()
    songs = len(data)

    return songs


def count_songs_by_key(key):
    """
    Challenge 2: Write a script that identify the number of songs in the key of E.
    """
    data = read_spotify_data()
    songs = len(data[data['key'] == key])

    return songs


def count_max_ocurrences_artist(key):
    """
    Challenge 3: Count the occurrences of values in a specified column (e.g., artist names)
    and determine the most common value.
    """
    data = read_spotify_data()
    artist = data[key].value_counts().idxmax()

    return artist


songs_number = count_songs()
songs_in_E = count_songs_by_key('E')
max_artist = count_max_ocurrences_artist('artist(s)_name')


print('There are {} songs in the dataset.'.format(songs_number))
print('There are {} songs in the key of E.'.format(songs_in_E))
print('The artist with the most songs in the dataset is {}.'.format(max_artist))
