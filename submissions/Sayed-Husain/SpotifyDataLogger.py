# -*- coding: utf-8 -*-
"""
# Spotify Data Analysis Project

## Introduction
This project aims to analyze Spotify data from a CSV file (`spotify-2023.csv`). The main tasks involve loading the data and completing the following challenges.

**Challenges:**
1. Write a script to identify the number of songs in the file.
2. Write a script that identify the number of songs in the key of E.
3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

## Load Spotify Data
Let's start by loading the Spotify data from the CSV file using Pandas, a popular data manipulation library.
"""

import pandas as pd

# Load Spotify data from the CSV file
csv_file = 'spotify-2023.csv'
df = pd.read_csv(csv_file, encoding = 'ISO-8859-1')

# Display the first few rows of the DataFrame
df.head()

"""## Challenge 1: Identify the Number of Songs
To identify the number of songs in the file, we can simply count the rows in the DataFrame.
"""

# Challenge 1: Identify the number of songs in the file
num_songs = len(df)
print(f"Number of songs in the file: {num_songs}")

"""## Challenge 2: Identify the Number of Songs in the Key of E
Next, let's identify the number of songs in the key of E.
"""

# Filter songs in the key of E
key_of_e_songs = df[df['key'] == 'E']

# Count the number of songs in the key of E
number_of_songs_in_key_of_e = len(key_of_e_songs)

# Display the result
print(f"Number of songs in the key of E: {number_of_songs_in_key_of_e}")

"""## Challenge 3: Count the Occurrences of Artist Names
Lastly, let's count the occurrences of artist names and determine the most common artist.
"""

# Challenge 3: Count the occurrences of artist names and determine the most common artist
artist_counts = df['artist(s)_name'].value_counts()
most_common_artist = artist_counts.idxmax()
most_common_artist_count = artist_counts.max()

print(f"Most common artist: {most_common_artist}")
print(f"Number of songs by {most_common_artist}: {most_common_artist_count}")
