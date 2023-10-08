# HACKTOBERFEST-2023
# Python Code for FILE I/O CHALLENGE 3 (Done for artist names)

import csv  # Using csv module

artist_ctr={}   # Creating empty dictionary

with open("spotify-2023.csv","r") as song_file:
    read_data = csv.DictReader(song_file)
    for line in read_data:
        name_list = line["artist(s)_name"].split(", ")  
        for name in name_list:
            if name in artist_ctr:
                artist_ctr[name] = artist_ctr[name] + 1     # Incrementing name count
            else:
                artist_ctr[name] = 1    # Putting in count for new entry
    
    for i,j in artist_ctr.items():
        print(f"Artist name: {i}\nNumber of tracks: {j}\n\n")   # Printing artist name and number of tracks by them.

    compare=0   # comparison variable initialised
    for count in artist_ctr.values():
        if count >= compare:
            compare = count     # Updating comparison variable with most number of tracks by end of loop
    
    artist_name = "".join([n for n, name_key in artist_ctr.items() if name_key == compare])    # Retieving artist name for the most number of tracks and making it a string 

    print(f"******The most songs are from: {artist_name}  (A total of {compare} tracks.)******")