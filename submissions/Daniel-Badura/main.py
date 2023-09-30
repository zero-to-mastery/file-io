import csv

csv_path = "spotify-2023.csv"


def count_songs(path):
    try:
        with open(path, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            song_counter = 0

            for row in csv_reader:
                song_counter += 1

            return song_counter

    except FileNotFoundError:
        return -404
    except Exception:
        return -400


if __name__ == "__main__":
    song_count = count_songs(csv_path)

    if song_count == -404:
        print("CSV file not found.")
    elif song_count == -400:
        print("Something went wrong.")
    else:
        print(f"Number of songs : {song_count}")
