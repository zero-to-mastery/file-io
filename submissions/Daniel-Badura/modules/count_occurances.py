import csv


def count_occurances(csv_file, column_name):
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header_row = next(csv_reader)

            if column_name not in header_row:
                print(f"Error: '{column_name}' column not found in the CSV header.")
                return None

            column_index = header_row.index(column_name)
            occurrences = {}

            for row in csv_reader:

                if column_index < len(row):
                    value = row[column_index]
                    if value not in occurrences:
                        occurrences[value] = 1
                    else:
                        occurrences[value] += 1


            most_common_value = max(occurrences, key=occurrences.get)
            most_common_count = occurrences[most_common_value]

            return most_common_value, most_common_count
    except FileNotFoundError:
        return None