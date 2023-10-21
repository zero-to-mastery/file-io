import pandas as pd

# Reading the csv file
df = pd.read_csv('spotify-2023.csv')

# Solution 1 function
def numberOfSongs(data):
    numberOfSongs = len(data)
    print('The number of songs is', numberOfSongs, '.' )

# Solution 2 function
def countKeyValue (data, column, value):
    digit = data[column].value_counts()[value]
    print('The number of', value, 'value is', digit, '.')

# Solution 3 function
def topArtist (data, column):
    digits = data[column].str.split(', ').explode().value_counts()
    top = digits.idxmax()
    print('Top artist is', top, '.')

# Solution 1:
numberOfSongs(df)

# Solution 2:
countKeyValue(df, 'key', 'E')

# Solution 3:
topArtist(df, 'artist(s)_name')