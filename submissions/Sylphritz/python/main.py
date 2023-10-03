import pandas as pd


def main():
    data = pd.read_csv('spotify-2023.csv')

    e_key_songs = data[data['key'] == 'E']
    song_count_by_artist = data['artist(s)_name'].value_counts()
    most_songs_index = song_count_by_artist.idxmax()

    print(f'There are total of {len(data)} songs in the dataset.')
    print(f'There are {len(e_key_songs)} songs in E key.')
    print(
        f'The artist with the most songs is {most_songs_index} with {song_count_by_artist[most_songs_index]} songs')


if __name__ == '__main__':
    main()
