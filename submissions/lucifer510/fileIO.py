import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('spotify-2023.csv')

# TODO TASK 1 : Write a script to identify the number of songs in the file.
# Count the number of songs
num_songs = len(df)
print("Number of songs in the file:", num_songs)

# TODO TASK 2 : Write a script that identify the number of songs in the key of E.
# Filter songs in the key of E
# Replace 'key' with the actual column name for key
e_songs = df[df['key'] == 'E']

# Count the number of songs in the key of E
num_e_songs = len(e_songs)
print("Number of songs in the key of E:", num_e_songs)


# TODO TASK 3 : Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
column_to_count = 'released_year'

# Count occurrences of values in the specified column
value_counts = df[column_to_count].value_counts()

# Get the most common value
most_common_value = value_counts.idxmax()

print(f"Occurrences of values in '{column_to_count}':")
print(value_counts)
print(
    f"The most common value in '{column_to_count}' is '{most_common_value}' with {value_counts.max()} occurrences.")
