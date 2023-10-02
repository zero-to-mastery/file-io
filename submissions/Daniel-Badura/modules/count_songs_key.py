import csv


def count_songs_key(csv_file, key_column, key_value):
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header_row = next(csv_reader)

            if key_column not in header_row:
                print(f"Error: '{key_column}' column not found in the CSV header.")
                return 0

            key_index = header_row.index(key_column)
            key_count = 0

            for row in csv_reader:
                if key_index < len(row):
                    if row[key_index] == key_value:
                        key_count += 1

            return key_count
    except FileNotFoundError:
        return 0