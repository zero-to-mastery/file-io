import pandas as pd


class SpotifyPlayList:
    """Manage operations with play list."""

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def get_songs_quantity(self) -> int:
        """Return quantity of songs in the play list."""

        return len(self.df)

    def get_value_count(self, column_name: str, value: str) -> int:
        """Return number of occurrences of the value in the column."""

        column_data = self.df.loc[:, column_name]

        return column_data.value_counts()[value]

    def get_most_frequent_value(self, column_name: str) -> tuple:
        """Return the most frequent value in the column."""

        column_data = self.df.loc[:, column_name]

        all_counts = column_data.value_counts(ascending=False)
        max_value = all_counts.index[0]
        max_value_count = all_counts.iloc[0]

        return max_value, max_value_count


playlist = SpotifyPlayList('spotify-2023.csv')
artist, qty = playlist.get_most_frequent_value('artist(s)_name')

print(f'There are {playlist.get_songs_quantity()} songs in this list.')

print(f'There are {playlist.get_value_count("key", "E")} songs '
      f'in the key of E.')

print(f'The most popular artist is {artist} with {qty} songs.')
