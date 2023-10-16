import sys
from collections import Counter
import numpy as np
import pandas as pd


def count_total_songs(data):
    total_songs = data['track_name'].count()
    return total_songs


def count_songs_with_key(data, key):
    songs_count_with_key = data['key'].value_counts()[key]
    return songs_count_with_key


def get_most_frequent_artists(data):
    # Get artists list for each track (string value containing artists as comma separated values)
    artists_list_per_track = data['artist(s)_name'].tolist()
    
    # Split the artists string around ',' and remove whitespaces to get 2D list of single artists
    artists_list = [[artist.strip() for artist in artists.split(',')] for artists in artists_list_per_track]
    
    # Convert 2D artists list to 1D list
    artists = list(np.concatenate(artists_list).flat)

    # Generate frequency map (dictionary) of artists
    artists_count = dict(Counter(artists))

    # Get list of most frequent artists
    max_count = max(artists_count.values())
    most_frequent_artists = [artist for artist,count in artists_count.items() if count == max_count]

    return most_frequent_artists, max_count
    


if __name__ == "__main__":
    csv_file_path = "spotify-2023.csv"
    data = pd.read_csv(csv_file_path)

    # Challenge-1 : Identify number of songs
    total_songs = count_total_songs(data)
    print("Total count of songs : " + str(total_songs))
    
    # Challenge-2 : Identify number of songs in the key of E
    key = "E"
    count = count_songs_with_key(data, key)
    print("Count of Songs with key '" + key + "' : " + str(count))

    # Challenge-3 : Count occurrences of values in column "artist(s)_name" & find most common value
    most_common_artists, count = get_most_frequent_artists(data)
    print("Most common artist(s) are : ", end="")
    for artist in most_common_artists:
        print(artist, ", ", sep="", end="")
    print("with count of " + str(count))
    
