import csv

fobj = open("spotify-2023.csv",encoding='latin-1')

robj = csv.reader(fobj)

def count_songs():
    count = -1 # To not include the header row
    for line in robj:
        count += 1
    return count

# print(count_songs())

def count_songs_in_key(key):
    
    if key[0] not in ["A","B","C","D","E","F","G"]:
        return "Invalid Key"
    
    count = 0
    for line in robj:
        if line[15] == key:
            # print("Song Title: "line[0])
            count += 1
    return count

# print(count_songs_in_key("A"))

def count_occurances(column_name):
    count_dictionary = {}
    for line in robj:
        if len(count_dictionary) == 0:
            # Getting the index of the column name from the header row
            search_column = line.index(column_name)
        if line[search_column] in count_dictionary:
            count_dictionary[line[search_column]] += 1
        else:
            count_dictionary[line[search_column]] = 1
    max_value = max(count_dictionary, key=count_dictionary.get)
    return max_value, count_dictionary[max_value]

# print(count_occurances("artist(s)_name"))