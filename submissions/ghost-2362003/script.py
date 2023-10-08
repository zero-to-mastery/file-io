import csv

# Specifying the file with path
filename = "spotify-2023.csv"

# Creating a dictionary to store the column indices
column_indices = {}
# Creating a list to store all the records of a file
file_contents = []

# Function which reads the file and stores data in the dictionary and list
def determine_column_indices():
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        
        # Store the indices that correspond to column titles
        for row in csv_reader:
            titles = row
            break
        index = 0
        for title in titles:
            column_indices[title] = index
            index += 1

        # Store the rest of the records except for the title in the list
        for row in csv_reader:
            file_contents.append(row)

# ========== CHALLENGE 1 ==========
# Write a script to identify the number of songs in the file.
def total_songs_in_file():
    return len(file_contents)

# ========== CHALLENGE 2 ==========
# Write a script that identify the number of songs in the key of E.
def total_songs_in_key(key):
    count = 0
    for song in file_contents:
        if song[column_indices["key"]] == key:
            count += 1
    return count

# ========== CHALLENGE 3 ==========
# Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
def count_most_common_value(column_name):
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)

        occurences = {}
        for row in csv_reader:
            value = row[column_name]
            if value in occurences:
                occurences[value] += 1
            else:
                occurences[value] = 1

        return max(occurences, key=occurences.get)

# Running the scripts
determine_column_indices()
# Printing the outputs of the challenges to the console
print("====================================")
print("Challenge 1 output: ", total_songs_in_file())
print("Challenge 2 output: ", total_songs_in_key("E"))
print("Challenge 3 output: ", count_most_common_value("artist(s)_name"))
print("====================================")