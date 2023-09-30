from modules.count_songs import count_songs
from modules.count_songs_key import count_songs_key

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
    key_column = "key" # You can modify the column
    key_value = "E"    # and the value to be counted

    songs_in_key = count_songs_key(csv_path, key_column, key_value)
    print(f"Number of songs in the key of E: {songs_in_key}")