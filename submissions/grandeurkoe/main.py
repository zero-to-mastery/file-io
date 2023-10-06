import pandas

FILENAME = "spotify-2023.csv"

# Change COUNT_COLUMN_NAME to count the occurrence of values.
# Change COMMON_COLUMN_NAME to determine the most common value.
# Possible values for COLUMN_NAME -
# track_name, artist(s)_name, artist_count, released_year, released_month, released_day,in_spotify_playlists,
# in_spotify_charts, streams, in_apple_playlists, in_apple_charts, in_deezer_playlists,
# in_deezer_charts, in_shazam_charts, bpm, key, mode, danceability_%, valence_%, energy_%, acousticness_%,
# instrumentalness_%, liveness_%,speechiness_%
COMMON_COLUMN_NAME = "artist(s)_name"
COUNT_COLUMN_NAME = "track_name"
SEARCH_VALUE = "Anti"


# Below identify_count() will compare SEARCH_KEY with each track name.
# For example,
#               It will compare "Anti" SEARCH_VALUE with the first four letters of each track name.
#               If True then it will increase key_count by 1.
def identify_count(all_data, value, data_column):
    """Identify number of songs in a column with a given value. Return number of songs."""
    key_count = 0
    for data in all_data[data_column]:
        # Convert to lowercase to avoid case sensitivity.
        if data[0: len(value)].lower() == value.lower():
            key_count += 1

    if key_count is None:
        return 0
    else:
        return key_count


def most_common_value(all_data, data_column):
    """Get most common value in a given column"""
    common_key = all_data[data_column].value_counts().index[0]
    return common_key


# Pandas read_csv() imports the 'spotify-2023.csv' file to a DataFrame object.
# Store this DataFrame object in a spotify_data variable.
spotify_data = pandas.read_csv(filepath_or_buffer="../../spotify-2023.csv")

# Log the results onto the console.
print(f"There are {len(spotify_data.index)} songs in '{FILENAME}' file.")
print(f"There are {identify_count(spotify_data, 'E', 'track_name')} songs in '{FILENAME}' file with key 'E'.")
print(f"There are {identify_count(spotify_data, SEARCH_VALUE, COUNT_COLUMN_NAME)} occurrences of '{SEARCH_VALUE}' "
      f"value in"
      f" '{COUNT_COLUMN_NAME}' column.")
print(f"The most common value in '{COMMON_COLUMN_NAME}' column is "
      f"'{most_common_value(spotify_data, COMMON_COLUMN_NAME)}'.")
