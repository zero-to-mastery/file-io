import pandas as pd
import numpy as np
from collections import Counter


def main():
    # get the csv file
    spotify_data = pd.read_csv("spotify-2023.csv", encoding="ISO-8859-1")

    # Challenge 1
    songs = spotify_data["track_name"]
    print(f"The total songs in the spotify csv file are: {len(songs)}")

    # Challenge 2
    songs_key_E = spotify_data[spotify_data["key"] == "E"]
    print(f"There are {len(songs_key_E)} songs in Spotify CSV where key is E")

    # Challenge 3

    art = spotify_data["artist(s)_name"]
    art_a = np.array(art)
    art_list = art_a.tolist()
    art_counts = Counter(art_list)
    most_common_art = art_counts.most_common(1)
    print(f"The most common artist is {most_common_art[0][0]}")


if __name__ == "__main__":
    main()
