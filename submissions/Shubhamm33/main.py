import pandas as pd
import os
from collections import Counter

def main():

    parent_directory = os.path.dirname(os.getcwd())
    grandparent_directory = os.path.dirname(parent_directory)
    list_dir = os.listdir(grandparent_directory)

    file = None
    
    # Reading file from outer directory 
    for f in list_dir:
        if f == 'spotify-2023.csv':
            file = f
    
    # if not present in outer directory read from current folder
    if file == None:
        file = 'spotify-2023.csv'

    # create dataframe
    df = pd.read_csv(file)

    challenge_1 = get_number_of_songs(df)
    challenge_2 = get_songs_in_name_of_key(df, 'E')
    challenge_3 = get_occurences(df, 'artist(s)_name')
    
    print("\n")
    print(challenge_1, "\n")
    print(challenge_2, "\n")
    print(challenge_3)
    print("\n")


def get_number_of_songs(df: pd.DataFrame):
    """Pass dataframe to get total number of songs"""
    return f"There are {len(df)} songs in this list"

def get_songs_in_name_of_key(df: pd.DataFrame, key: str):
    """Pass dataframe and key to get total songs in that particular key"""
    df = df[df['key'] == key]
    return f"There are {len(df)} songs in the key of E"

def get_occurences(df: pd.DataFrame, column_name: str):
    """Pass dataframe and any column name to get its occurence"""
    # check columns
    # print(df.columns)
    try:
        if column_name in df.columns:
            col_list = df[column_name].tolist()
            counter = Counter(col_list)
            common_occurence = counter.most_common(1)
            return f"Most common occurence for column name '{column_name}' has value '{common_occurence[0][0]}' and occured {common_occurence[0][1]} times"
            
        else:
            return "Column Not present, please check column name"
    except Exception as e:
        return f"Error: {e.__str__()}"


if __name__ == '__main__':
    main()