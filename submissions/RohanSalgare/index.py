import pandas as pd
import csv


def total_num_of_songs():
    df = pd.read_csv('spotify-2023.csv', encoding='latin1')
    return len(df)

def number_of_songs_in_key(key):
    with open('spotify-2023.csv', 'r'
    ,encoding='latin1') as file:
        reader = csv.reader(file)
        columns = next(reader)
        #storing the index of element 'key' in index variable
        index = columns.index('key')

        num_of_songs = 0
        for row in reader:
            if row[index] == key:
                num_of_songs += 1

        file.close()
    return num_of_songs


print(f"Total Number of songs : {total_num_of_songs()}")
print(f"Total Number of songs in Key: {number_of_songs_in_key('E')}")

