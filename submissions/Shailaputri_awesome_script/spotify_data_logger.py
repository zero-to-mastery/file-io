"""
Spotify Data Logger : A data processing file I/O script that reads data from a CSV file 
containing spotify data and performs some analysis to complete one or more of the 
challenges outlined below.
Challenges:
    ONE - Write a script to identify the number of songs in the file.
    TWO - Write a script that identify the number of songs 
    in the key of E.
    THREE - Count the occurrences of values in a specified column 
    (e.g., artist names) and determine the most common value.

The script reads data from "spotify-2023.csv". It identifies number of 
songs in file, number of
songs in any specified key and also counts the occurrence of value
 in specified column. 

This is a completely modular code. By this I mean:
1. User can provide how many rows from the file needs to be 
processed. By default, the script processes the 
entire CSV file. 
2.Strategy Design has been used to add to accomodate any change in future
requirements of finding count of occurrences in more columns. 
3.Code adheres to OOPs SOLID principles. Only the required APIs have been exposed viz:
    --> Process file by providing how many entries need to be processed.
    --> GET count of songs in CSV (COMPLETES CHALLENGE ONE)
    --> GET songs in a particular key (COMPLETES CHALLENGE TWO. This also takes care of
    future requirement of change in key other than 'E')
    --> GET count of occurrences of specified column (COMPLETES 
    CHALLENGE THREE)
4. No frameworks used. This script is executable through CLI. It 
stores data in memory using Hashmap as the only data structure. 

Comments on code are super welcome!
"""


import csv
from collections import defaultdict
from abc import ABC, abstractmethod
import sys


class FileProcessor:
    """
    Processes input CSV fule using DictReader.

    Gives option to user to select the number of rows
    from the file that should be processed. By default
    processes the entire file.

    >>> get_song_count()
    953

    >>> get_particular_key_count('E')
    62

    """

    def __init__(self):
        self.count = None
        self.spotify_row = []
        self.artists_count = defaultdict(int)
        self.key_count = defaultdict(int)
        self.released_year_count = defaultdict(int)
        self.list_of_column_names = []

    def process_file(self, count=sys.maxsize):
        i = 0
        self.count = count
        with open("spotify-2023.csv", "r", newline="", encoding="Latin-1") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if i > self.count:
                    break
                self.spotify_row.append(row)
                i += 1
                self.artists_count[row["artist(s)_name"]] += 1
                self.released_year_count[row["released_year"]] += 1
                self.key_count[row["key"]] += 1

    def get_song_count(self):
        return len(self.spotify_row)

    def get_particular_key_count(self, keynote):
        return self.key_count[keynote]

    def get_key_count(self):
        return self.key_count

    def get_artist_count(self):
        return self.artists_count

    def get_year_count(self):
        return self.released_year_count


class DataProcessorStrategy(ABC):
    """
    Abstract strategy class. Different DataProcessor classes
    that inherit this class also implement the abstract
    methods of this abstract class.
    """

    @abstractmethod
    def count_occurrences(self):
        pass


class KeyDataProcessor(DataProcessorStrategy):
    def count_occurrences(self):
        maxCount, maxCountKey = float("-inf"), []
        keyCount = fileProcessor.get_key_count()
        for key, count in keyCount.items():
            if count == maxCount:
                maxCountKey.append(key)
            elif count > maxCount:
                maxCountKey = [key]
                maxCount = count
            else:
                continue

        mostCommonKeys = ",".join(maxCountKey)
        print(f"The most common key is/are {mostCommonKeys} with {maxCount} songs.")


class ArtistsDataProcessor(DataProcessorStrategy):
    def count_occurrences(self):
        maxCount, maxCountArtist = float("-inf"), []
        artistsCount = fileProcessor.get_artist_count()
        for artist, count in artistsCount.items():
            if count == maxCount:
                maxCountArtist.append(artist)
            elif count > maxCount:
                maxCountArtist = [artist]
                maxCount = count
            else:
                continue
        mostCommonArtists = ",".join(maxCountArtist)
        print(
            f"The most popular artist is/are {mostCommonArtists} with {maxCount} songs."
        )


class YearDataProcessor(DataProcessorStrategy):
    def count_occurrences(self):
        maxCount, maxCountYear = float("-inf"), []
        yearCount = fileProcessor.get_year_count()
        for year, count in yearCount.items():
            if count == maxCount:
                maxCountYear.append(year)
            elif count > maxCount:
                maxCountYear = [year]
                maxCount = count
            else:
                continue
        mostCommonYear = ",".join(maxCountYear)
        print(f"The most common year is/are {mostCommonYear} with {maxCount} mentions.")


class SpotifyDataLogger:
    """
    Most important class to log data of different columns.
    This has been made completely customisable. User can find
    count of occurrences of any column among
    Key, Artist and Released_Year. In future, the number of
    such columns can also be increased.

    """

    def count_occurrences(self, col_name):
        dataProcessorFactory = DataProcessorFactory()
        dataProcessorStrategy = dataProcessorFactory.get_data_processor(col_name)
        dataProcessorStrategy.count_occurrences()


class DataProcessorFactory:
    def __init__(self):
        self.keyDataProcess = KeyDataProcessor()
        self.artistDataProcess = ArtistsDataProcessor()
        self.yearDataProcess = YearDataProcessor()

    def get_data_processor(self, col_name):
        if col_name == "Key":
            return self.keyDataProcess
        elif col_name == "Artist":
            return self.artistDataProcess
        elif col_name == "Year":
            return self.yearDataProcess
        else:
            print("Invalid")


class ColumnNames:
    """
    This is an optional class to find the column list in the CSV.
    It is not instantiated in the script here.
    """

    def __init__(self):
        self.list_of_column_names = []
        self.no_of_rows = 0

    def process(self):
        with open("spotify-2023.csv", "r", newline="", encoding="Latin-1") as file:
            csv_reader = csv.DictReader(file)
            dict_from_csv = dict(list(csv_reader)[0])
            self.list_of_column_names = list(dict_from_csv.keys())

            # enum_list_of_column = Enum('enum_list_of_column', list_of_column_names)
            # print(dir(enum_list_of_column))

    def __str__(self):
        return f"Column List : {self.list_of_column_names}"


if __name__ == "__main__":
    """
    Steps to follow :

    For Challenge 1 & 2:
    Instantiate FileProcessor.
    Specify the number of rows to be processed.
    Specify the note whose count of songs is needed (
    mentioned as 'E' in challenge)

    For Challenge 3:
    Instantiate SpotifyDataLogger.
    Provide the column name whose count of occurrences is needed.
    """

    fileProcessor = FileProcessor()
    no_of_rows_to_process = sys.maxsize
    # no_of_rows_to_process = 10
    fileProcessor.process_file(no_of_rows_to_process)
    # Challenge 1 : Identify the number of songs in file
    songs = fileProcessor.get_song_count()
    print(f"There are {songs} songs in this file.")
    # Challenge 2 : Identify number of songs in the key of E
    note = "E"
    songs = fileProcessor.get_particular_key_count(note)
    print(f"There are {songs} songs in the key of {note}")
    # Challenge 3 : Count occurrences of values in a specified column
    # and determine the most common value
    specified_column = "Key"
    spotifyDataLogger = SpotifyDataLogger()
    spotifyDataLogger.count_occurrences(specified_column)
