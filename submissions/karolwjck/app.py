"""

Create a data processing file I/O script that reads data from a CSV file containing Spotify data and performs some analysis to 
complete one or more of the challenges outlined below.

The project is flexible enough to work with nearly any backend programming language. 
This README provides an overview of the project and explains how to adapt it to your chosen programming language.


Project Overview
    The project consists of a script that reads data from a CSV file (spotify-2023.csv) and performs the following tasks.
    Load Spotify data from the CSV file.
    Create a folder for your project with your github handler.
    Complete at least one of the challenges below.
    Add your folder with your project to the submissions folder of this repo.
    Include the script that runs your file.

    Note: the project must successfully complete one of the challenges below to qualify for as a submission.

    
Challenges
    1) Write a script to identify the number of songs in the file.
    2) Write a script that identify the number of songs in the key of E.
    3) Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

    
How to run?
    1) In the root directory do cd .\submissions\karolwjck\
    2) Run the script python app.py

"""


import csv
from collections import Counter


spotify_2023 = 'spotify-2023.csv'


def num_songs_in_file(file_path):
    with open(file_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        
        next(csv_reader)
        num_songs = sum(1 for _ in csv_reader)
        
        return num_songs


def num_songs_key_of_e(file_path):
    with open(file_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        
        next(csv_reader)
        key_of_e_count = sum(1 for row in csv_reader if row[15] == 'E')
        
        return key_of_e_count


def most_common_artist(file_path):
    with open(file_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)

        next(csv_reader)
        artist_names = [row[1] for row in csv_reader]
        artist_counts = Counter(artist_names)
        most_common_artist, count = artist_counts.most_common(1)[0]

        return most_common_artist, count


if __name__ == '__main__':
    num_songs = num_songs_in_file(spotify_2023)
    print(f"Number of songs in the file: {num_songs}")
    
    num_songs_e = num_songs_key_of_e(spotify_2023)
    print(f"Number of songs in the key of E: {num_songs_e}")
    
    most_common_artist_name, artist_count = most_common_artist(spotify_2023)
    print(f"Most common artist: {most_common_artist_name} (Appears {artist_count} times)")

