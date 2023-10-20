import pandas as pd
import matplotlib.pyplot as plt

# Read csv file in pandas Dataframe
spotify = pd.read_csv("spotify-2023.csv", encoding="latin-1")


# Number of songs in csv file
def number_of_songs(spotify):
    return spotify.shape[0]


def songs_keye(spotify):
    return len(spotify[spotify["key"] == "E"])


# Find the most common artists in csv file
def common_track_name(spotify):
    return spotify["track_name"].mode().tolist()


print("The total number of songs in the file: ", number_of_songs(spotify))
print("The number of songs in the key of 'E': ", songs_keye(spotify))
print(
    "The track names occuring more than once in the file:", common_track_name(spotify)
)
