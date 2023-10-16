import csv

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