import re


def main():
    # Load and clean the data

    data = open('spotify-2023.csv', 'r')

    # Split data by row
    rows = data.readlines()

    # Strip new line characters (\n) and split data into columns

    # This RegEx is to prevent splitting columns with commas in the column value
    strip_pattern = r'(?:,|^)(?=[^"]|(")?)"?((?(1)[^"]*|[^,"]*))"?'

    def split_columns(row):
        new_row = []
        # Split the row into columns and also remove the line break character at
        columns = [column[1]
                   for column in re.findall(strip_pattern, row.strip('\n'))]

        for col in columns:
            if not col is None:
                new_row.append(col.strip('"'))

        return new_row

    # Strip out the first row (the column headers)
    rows = list(map(split_columns, rows))[1:]

    # Declaring important column indexes
    ARTIST_NAME_INDEX = 1
    KEY_INDEX = 15

    songs_in_e_key_count = 0

    # Loop through rows and count the ones in E key
    for row in rows:
        if row[KEY_INDEX].lower() == 'e':
            songs_in_e_key_count += 1

    # Declare a dictionary for keeping track of song counts
    song_counts = {}

    # Loop through each row
    for row in rows:
        artist_name = row[ARTIST_NAME_INDEX]

        # Increment the count for each occurrence of songs by an artist
        if artist_name in song_counts.keys():
            song_counts[artist_name] += 1
        else:
            song_counts[artist_name] = 1

    # Get the max count
    max_song_count = max(list(song_counts.values()))
    # Find the index of the max value and map it to the artist's name
    artist_with_most_songs = list(song_counts.keys())[list(
        song_counts.values()).index(max_song_count)]

    # Print the results
    print(f'There are total of {len(rows)} songs in the dataset.')
    print(f'There are {songs_in_e_key_count} songs in E key.')
    print(
        f'The artist with the most songs is {artist_with_most_songs} with {max_song_count} songs')


if __name__ == '__main__':
    main()
