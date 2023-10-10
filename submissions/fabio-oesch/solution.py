import csv
from typing import Dict

def main():
    song_per_artist:Dict[str, int] = dict[str, int]()
    in_e_key:int = 0
    song_amount:int = 0
    with open('../../spotify-2023.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row["key"] == "E": # count number of songs in E key
                in_e_key += 1
            for artist_name in row["artist(s)_name"].split(","): # split artists name and add them to dictionary
                artist_name = artist_name.strip()
                song_per_artist[artist_name] = song_per_artist.get(artist_name, 0) + 1
            song_amount += 1
            


    artist_with_most_songs:str = max(song_per_artist, key=song_per_artist.get)
    print("Songs in E key: " + str(in_e_key))
    print("Songs in total: " + str(song_amount))
    print("Artist with most songs: " + artist_with_most_songs + " with " + str(song_per_artist[artist_with_most_songs]) + " songs")
              
if __name__ == "__main__":
    main()





