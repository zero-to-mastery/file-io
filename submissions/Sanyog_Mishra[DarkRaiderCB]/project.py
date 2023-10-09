# HACKTOBERFEST-2023
# Python Code for FILE I/O CHALLENGE 1

import csv  #Using csv module
with open("spotify-2023.csv","r") as song_file:
    read_data = csv.reader(song_file)
    next(read_data)
    ctr=0   #initialising Counter
    for line in read_data:  
        ctr=ctr+1
    print(f"The total number of songs in spotify-2023.csv are: {ctr}")


