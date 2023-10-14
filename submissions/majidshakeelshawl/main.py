import pandas as pd

def main():
    # get the csv file
    spotify_data = pd.read_csv('spotify-2023.csv',encoding='ISO-8859-1')
    songs = spotify_data['track_name']
    print(f"The total songs in the spotify csv file are: {len(songs)}")
    
if __name__ == '__main__':
    main()