import pandas as pd


class CsvCounter:
    """Calculations in .csv file."""

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def count_length(self, column_name: str = None) -> int:
        """Return quantity of rows in a column or in whole dataframe."""

        if column_name:
            column_data = self.df.loc[:, column_name]
            return len(column_data)

        return len(self.df)

    def count_value_frequency(self, column_name: str, value: str) -> int:
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


counter = CsvCounter('spotify-2023.csv')
artist, qty = counter.get_most_frequent_value('artist(s)_name')

print(f'There are {counter.count_length("track_name")} songs in this list.')
print(f'There are {counter.count_value_frequency("key", "E")} songs '
      f'in the key of E.')
print(f'The most popular artist is {artist} with {qty} songs.')
