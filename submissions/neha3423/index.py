import pandas as pd

df=pd.read_csv('spotify-2023.csv', encoding='latin-1')

# Number of songs in csv
def number_of_songs(df):
  return df.shape[0]

#Number of songs in the key of E
def songs_in_key_of_E(df):
  songs=df[df['key']=='E']
  return len(songs)

#Determine the most common artist
def most_common_artist(df):
  count= df['artist(s)_name'].mode().tolist()
  return count

print("The total number of songs in the playlist:",number_of_songs(df))
print("The number of songs in the key of E:",songs_in_key_of_E(df))
print("The most common artist in the playlist:",most_common_artist(df))