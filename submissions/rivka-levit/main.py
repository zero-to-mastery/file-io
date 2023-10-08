import pandas as pd

# Read the data from csv file
use_cols = ['track_name', 'artist(s)_name', 'key']
df = pd.read_csv('spotify-2023.csv', usecols=use_cols)

# Count the values
songs_qty = df.count('rows')['track_name']
e_qty = df['key'].value_counts()['E']

# Log the results to the console
print(f'There are {songs_qty} songs in this list.')
print(f'There are {e_qty} songs in the key of E.')
for artist, qty in df['artist(s)_name'].value_counts(ascending=False).items():
    print(f'The most popular artist is {artist} with {qty} songs.')
    break
