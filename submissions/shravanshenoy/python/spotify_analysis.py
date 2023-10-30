import pandas as pd 

SPOTIFY_FILE_PATH = 'spotify-2023.csv'

def spotify_analysis():
    #spotify_df = pd.read_csv(SPOTIFY_FILE_PATH, encoding='cp1252')
    spotify_df = pd.read_csv(SPOTIFY_FILE_PATH)

    #Challenge 1
    num_songs = spotify_df['track_name'].nunique()

    #Challenge 2
    num_songs_e = spotify_df[spotify_df['key'] == 'E']['track_name'].nunique()

    #Challenge 3
    most_occurences = spotify_df['artist(s)_name'].value_counts().index[0]


    ############ Results

    print(f"Number of songs in file is : {num_songs}")

    print(f"Number of songs in key of E is : {num_songs_e}")

    print(f"Value with highest occurence in artist(s) name column is : {most_occurences}")



if __name__ == '__main__':
    spotify_analysis()