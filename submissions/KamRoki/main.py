# Read CSV file
import pandas as pd

df = pd.read_csv('/Users/kamil/Machine-Learning/file-io/file-io/submissions/KamRoki/spotify-2023.csv', delimiter = ',', encoding="ISO-8859-1")

# Challange 1
number_of_songs = len(df)
print('Number of songs in Spotify file: ', number_of_songs)