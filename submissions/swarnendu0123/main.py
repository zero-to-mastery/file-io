import pandas as pd
df = pd.read_csv("./spotify-2023.csv")

# function to get all songs
def get_all_songs(df):
    songs = df["track_name"]
    return list(songs)

# function to search songs by its key
def get_songs_in_key(df, key):
    songs = df[(df["key"] == key)]
    return songs

# function to get unique songs
def get_unique_songs(df):
    unique_songs = df["track_name"].unique()
    return unique_songs

# function to get all unique artist
def get_unique_artists(df):
    unique_artists = []
    for i in range(len(df["artist(s)_name"])):
        unique_artists.extend(df["artist(s)_name"][i].split(", "))
    unique_artists = set(unique_artists)
    return unique_artists

# function to get all unique artist
def get_all_artists(df):
    unique_artists = []
    for i in range(len(df["artist(s)_name"])):
        unique_artists.extend(df["artist(s)_name"][i].split(", "))
    return pd.Series(unique_artists)

# Challenge 1: Identify the number of songs in the file
print("Total number of songs:", len(get_all_songs(df)))
# Challenge 2: Identify the number of songs in the key of E
key = input("Enter the key, to search songs: ")
print("the number of songs in the key of",
      key, ":", len(get_songs_in_key(df, key)))
# Challenge 3: Count the occurrences of artist names and find the most common value
print("Number of unique songs:", len(get_unique_songs(df)))
print("Number of unique artists:", len(get_unique_artists(df)))
print("Number of common artists:", get_all_artists(df).mode()[0])