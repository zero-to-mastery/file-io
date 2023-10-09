import csv

file_path = '../../spotify-2023.csv'

track_name_column_index = 0
artist_column_index = 1
key_column_index = 15

songs = []
songs_key_e = []
artist_hash = {}

with open(file_path, newline='', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    try:
        for row in csv_reader:
            if csv_reader.line_num > 1:
                song = row[track_name_column_index]
                artist = row[artist_column_index]
                if song not in songs: #songs not repeated
                    songs.append(song)
                if song not in songs_key_e and row[key_column_index]=='E': #songs not repeated
                    songs_key_e.append(song)
                if artist_hash.get(artist):
                    artist_hash[artist] +=1
                else:
                    artist_hash[artist] = 1
            else:
                print(row)
    except csv.Error as e:
        print('file {}, line {}: {}'.format(file_path, csv_reader.line_num, e))

print(f"The number of songs in the file is {len(songs)}!")
print(f"The number of songs in the key of E is {len(songs_key_e)}!")
most_common_value = max(artist_hash, key=artist_hash.get)
print(f"The most common value in artist names is {most_common_value}, with a total of {artist_hash[most_common_value]}!")


#cleaning vars
songs = []
songs_key_e = []
artist_hash.clear()