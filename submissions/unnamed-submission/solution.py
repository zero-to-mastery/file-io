# import module
import pandas as pd

def count_songs_with_key(data):
    counts = data['key'].value_counts()['E']
    return counts

def count_occurences_of_values(data):
    dict = {}
    artists = data['artist(s)_name']

    for artist in artists:
        name = ""
        for x in artist:
            if x != ',':
                name+=x
            else:
                name = name.strip()
                if dict.get(name) == None:
                    dict[name] = 1
                else:
                    dict[name] = dict[name] + 1
                name=""
        name = name.strip()
        if dict.get(name) == None:
            dict[name] = 1
        else:
            dict[name] = dict[name] + 1
     
    keyMax = max(zip(dict.values(), dict.keys()))[1]
    return(keyMax)

# read the csv file
results = pd.read_csv('spotify-2023.csv')  


# solution 1
numOfSongs = len(results)
print("Number of songs: ", numOfSongs)

# solution 2
numOfSongsWithE = count_songs_with_key(results)
print("Number of songs with key E: ", numOfSongsWithE)

# solution 3
mostOccurences = count_occurences_of_values(results)
print("Most streamed artist: ", mostOccurences)