import pandas as pd

# Load the file
df = pd.read_csv('./spotify-2023.csv', encoding='ISO-8859-1')

# Get the number of songs in the file
def num_of_songs(df):
    return len(df)

# Get the number of songs in the key of E
def number_of_key_e(df):
    return len(df[df['key'] == 'E'])

# Determining the most streamed song, what is it called, and who is the artist
def most_streamed(df):
    df1 = df.mode().iloc[0]
    artist_name = df1['artist(s)_name']
    track_name = df1['track_name']
    streams = df1['streams']
    return [streams, track_name, artist_name]

# Print the information
print("The number of songs in the csv file is: ", num_of_songs(df))
print("The number of songs in the key of 'E' in the csv file is: ",number_of_key_e(df))
song_info = most_streamed(df)
print("The biggest number of streams was: ", song_info[0] ," , it was a track called: ", song_info[1], " , by: ", song_info[2])
