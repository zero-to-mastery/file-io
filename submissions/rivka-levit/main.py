from countings.csv_counter import CsvCounter

counter = CsvCounter('data/spotify-2023.csv')
artist, qty = counter.get_most_frequent_value('artist(s)_name')

print(f'There are {counter.count_length("track_name")} songs in this list.')
print(f'There are {counter.count_value_frequency("key", "E")} songs '
      f'in the key of E.')
print(f'The most popular artist is {artist} with {qty} songs.')
