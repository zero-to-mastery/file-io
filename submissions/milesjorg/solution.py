import pandas as pd

# Counts the total number of songs in the csv file
def count_total_songs(file):
    return file["track_name"].count()

# Counts the total number of songs in the specified key
def count_songs_in_key(file, key="E"):
    total_songs_keys = file["key"]
    songs_in_key = 0
    for column in total_songs_keys:
        if column == key.upper():
            songs_in_key += 1
    return songs_in_key

def count_max_occurrences(file, column):
    data = file[column]
    occurences = {}
    max_count = 0
    highest_occurence = None

    for item in data:
        # For the case of artists names, split the values if multiple artists and add an occurrence to each respective artist listed
        datum = item.split(",")
        for i in datum:
            i = i.strip()
            try:
                occurences[i] += 1
                if occurences[i] > max_count:
                    max_count = occurences[i]
                    highest_occurence = (i, occurences[i])
            except KeyError:
                occurences[i] = 1
    return highest_occurence


file = pd.read_csv('spotify-2023.csv', encoding='latin-1')

print(f"Total number of songs: {count_total_songs(file)}")
# Change this value to desired key
key = "e"
print(f"Total number of songs in key {key.upper()}: {count_songs_in_key(file, key)}")
# Change this value to desired column
column = "artist(s)_name"
max_occurrences = count_max_occurrences(file, column)
print(f"The most occurrences for column {column} is {max_occurrences[0]} with {max_occurrences[1]} occurrences")