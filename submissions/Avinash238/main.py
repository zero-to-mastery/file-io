import pandas as pd

# Load Spotify data from the CSV file
df = pd.read_csv("spotify-2023.csv")

# Challenge 1: Identify the number of songs in the file
def get_number_of_songs(df):
    return len(df)

# Challenge 2: Identify the number of songs in the key of E
def get_number_of_songs_in_key_e(df):
    return len(df[df['key'] == 'E'])

# Challenge 3: Count the occurrences of artist names and find the most common value
def get_most_common_artist(df):
    return df['artist(s)_name'].mode().iloc[0]

# Print the results
print("Challenge 1: Total number of songs =", get_number_of_songs(df))
print("Challenge 2: Number of songs in the key of E =", get_number_of_songs_in_key_e(df))
print("Challenge 3: Most common artist =", get_most_common_artist(df))
