#1. Write a script to identify the number of songs in the file.
#2. Write a script that identify the number of songs in the key of E.
#3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

import sys
import os
def analysis(csvObject):
    try:
        header = next(csvObject)

        analyse_val={"num_songs":0,"num_songs_E":0, "artist_count":0, "artist_names":{}}
    
        for row in csvObject:
            number_of_songs(row,header,analyse_val)
            most_common_artist_name(row, header, analyse_val)
  
        print_results(analyse_val)    

    except Exception as e:
        print("Error in the 'analysis' function:", e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    
def number_of_songs(row, header,analyse_val):
    index_key = header.index('key')
    analyse_val['num_songs'] += 1
    key=row[index_key]
    if key=="E":   
        analyse_val['num_songs_E'] += 1
def most_common_artist_name(row, header, analyse_val):
    index_name = header.index('artist(s)_name')
    artist_name=row[index_name]
    artist_names=artist_name.split(',')
    for artist_name in artist_names:
        if artist_name not in analyse_val['artist_names']:
            analyse_val['artist_names'][artist_name]=1
        else:
            analyse_val['artist_names'][artist_name]+=1
         
        
def print_results(analyse_val):
    
    print("Number of songs:", analyse_val['num_songs'])
    print("Number of songs in key E:", analyse_val['num_songs_E'])
    
    sorted_dict = sorted(analyse_val['artist_names'].items(), key=lambda item:item[1], reverse=True)
    print("Most common artist name:", next(iter(sorted_dict))[0])