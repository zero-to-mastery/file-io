# Read CSV file
import pandas as pd

def count_key_e(data):
    counts = data.key.value_counts()['E']
    return counts

df = pd.read_csv('/Users/kamil/Machine-Learning/file-io/file-io/submissions/KamRoki/spotify-2023.csv', delimiter = ',', encoding="ISO-8859-1")

# Challange 1
number_of_songs = len(df)
print('Number of songs in Spotify file: ', number_of_songs)

# Challange 2
number_of_E = count_key_e(df)
print('Number of songs with key E: ', number_of_E)