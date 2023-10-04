import csv
from collections import Counter

songs = []
key = []
name = []


with open("./spotify-2023.csv", encoding="utf-8") as spotify_csv:
    reader = csv.reader(spotify_csv, delimiter=",")
    for line in reader:
        songs.append(line[0])
        key.append(line[15])
        name.append(line[1])


# * Write a script to identify the number of songs in the file.
def amount_of_songs():
    return f"There are {len(songs)} songs in the file"


# * Write a script that identify the number of songs in the key of E.
def songs_key_e():
    return f"there are {key.count('E')} songs in the key of E"


# * Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
def most_common_song():
    most_common_song = Counter(songs).most_common(1)
    return f"Most common song: {most_common_song}."


def most_common_key():
    most_common_key = Counter(key).most_common(1)
    return f"Most common key: {most_common_key}."


def most_common_name():
    most_common_name = Counter(name).most_common(1)
    return f"Most common artist name: {most_common_name}."


with open("new.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    field = ["extracted data from spotify.csv"]

    writer.writerow(field)
    writer.writerow([amount_of_songs()])
    writer.writerow([songs_key_e()])
    writer.writerow([most_common_song()])
    writer.writerow([most_common_key()])
    writer.writerow([most_common_name()])
