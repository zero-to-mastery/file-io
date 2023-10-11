import pandas as pd

# Read the CSV file into a pandas DataFrame with specified encoding
df = pd.read_csv('./spotify-2023.csv', encoding='ISO-8859-1')

def count_songs_in_key_of_e(dataframe):
    key_of_e_songs = dataframe[dataframe['key'] == 'E']
    return len(key_of_e_songs)

# Print the total number of songs in the file
print("Number of songs:", len(df))

# Print the number of songs in the key of E with appropriate text
print("Total Number in Key of E:", count_songs_in_key_of_e(df))
