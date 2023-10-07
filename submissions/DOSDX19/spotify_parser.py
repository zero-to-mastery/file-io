# import the pandas library and renames it as "pd" for convenience. 
#This library is essential for working with dataframes in Python.

import pandas as pd 

# read the CSV file into a pandas dataframe
df = pd.read_csv('spotify-2023.csv') #, usecols=['track_name']


def count_songs(column):

    """
    This function takes a specified column and returns the number of songs in that column.
    
    Parameters:
    -----------
    column : 
         The column containing the songs.
        
    Returns:
    --------
    count : int
        The number of songs in the specified column.
    
    Example:
    --------
    If we have a column named 'artist(s)_name' containing artist(s) name(s), we can use this function to count the number of names as follows:
    
    >>> count_songs(df["artist(s)_name"])
    100
    """
    
    number_of_song = column.value_counts().count()
    return number_of_song
    

def count_songs_in_key(df, key):
    """This function takes tow parameters a data frame object consist of tow column 
      with a specified key
      and returns number of songs has that specified key"""
    
    #Convert the data frame object values to list
    df_values = list(df.values)

    #Prepareing a set object that will contain the values to insure there is no duplication
    unique_e = set()

    #Looping throw the data frame values 
    for item in df_values:
        #check if the key comlumn value is equal to E
        if item[1] == key:
            #Adding the list item to the set object as a tuple
            unique_e.add((item[0],item[1]))

    #number of song variable contain the length of the set object which is the number of songs 
    number_of_song = len(unique_e)
    return number_of_song


def find_most_common_value(df, column):
    """ This function takes to parameters and returns back the most common artist with number of occurrencess."""
    # count the occurrences of each value in the specified column
    counts = column.value_counts()

    # get the most common value (i.e., the one with the highest count)
    most_common = counts.idxmax()

    return (f"The most common artist is {most_common} with {counts[most_common]} occurrences.")


print(f"There is {count_songs(column=df['track_name'])} songs in spotify-2023 file")
print(f"There is {count_songs_in_key(df[['track_name', 'key']], 'E')} songs in the key of 'E' in spotify-2023 file")
print(find_most_common_value(df,df['artist(s)_name']))