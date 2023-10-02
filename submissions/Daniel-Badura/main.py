from modules.count_songs import count_songs
from modules.count_songs_key import count_songs_key
from modules.count_occurances import count_occurances

csv_path = "spotify-2023.csv"

if __name__ == "__main__":
    # Challenge One
    song_count = count_songs(csv_path)

    if song_count == -404:
        print("CSV file not found.")
    elif song_count == -400:
        print("Something went wrong.")
    else:
        print(f"Number of songs : {song_count}")

    # Challenge Two
    column_name = "key"  # You can modify the column
    key_value = "E"  # and the value to be counted

    songs_in_key = count_songs_key(csv_path, column_name, key_value)
    print(f"Number of songs in the key of E: {songs_in_key}")

    # Challange Three

    result = count_occurances(csv_path, column_name)

    if result:
        most_common_value, most_common_count = result
        print(
            f"The most common value in the specified column is '{most_common_value}' with {most_common_count} occurrences."
        )
    else:
        print("An error occurred. Please check the CSV file and column name.")
