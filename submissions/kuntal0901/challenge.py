import csv
from collections import defaultdict


'''
Challenges:
    - Write a script to identify the number of songs in the file.
    - Write a script that identify the number of songs in the key of E.
    - Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
'''

artistsSpotify = [] # This array hold the data of each row of csv(songs data) i.e songs
numberSongswithKeyE = 0 # This keeps tracks of number of songs in the key of E
artistsCount = defaultdict(int)  # This hashmap(dictionary) keeps a track of artist_name with the number of songs the artist has sung present in the csv



with open('spotify-2023.csv', 'r', newline='', encoding='ISO-8859-1') as file:
    csv_reader = csv.DictReader(file)


    for song in csv_reader:
        artistsSpotify.append(song)
        if song['key'] == 'E':
            numberSongswithKeyE += 1
        artistsCount[song['artist(s)_name']] += 1

    # Challenge 1:
    numberOfSongs = len(artistsSpotify)
    print(f'There are {numberOfSongs} songs in this file')
    print('------------------------------------------------------------------')

    # Challenge 2:
    print(f'There are {numberSongswithKeyE} songs in the key of E.')
    print('------------------------------------------------------------------')

    # Challenge 3:
    maxCount,maxCountArtist = float('-inf'),[]

    for artist,count in artistsCount.items():
        if count == maxCount:
            maxCountArtist.append(artist)
        elif count > maxCount:
            maxCountArtist = [artist]
            maxCount = count
        else:
            continue


    mostCommonArtists = ','.join(maxCountArtist)[:-1]
    print(f'The most popular artist is/are {mostCommonArtists} with {maxCount} songs.')



