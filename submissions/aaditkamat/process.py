import pandas as pd

def number_of_songs_in_key(df: pd.DataFrame, key: str) -> int:
    return df[df['key'] == key]['track_name'].unique().size

def number_of_songs_in_file(df: pd.DataFrame) -> int:
   songs = df['track_name']
   return songs.unique().size

def count_occurences(df: pd.DataFrame, col_name: str) -> pd.Series:
   return df[col_name].value_counts()

def get_most_common_value(df: pd.DataFrame, col_name: str) -> str:
   return count_occurences(df, col_name).idxmax()

def get_col_name_user_input(df: pd.DataFrame) -> str:
   col_name = input('Enter a column name: ')
   if col_name not in df.columns:
      print('Enter a column that exists in the CSV file')
      return get_col_name_user_input(df)
   else:
      return col_name

if __name__ == '__main__':
    df = pd.read_csv('../../spotify-2023.csv')    
    print(f"Number of songs in the file: {number_of_songs_in_file(df)}")
    print(f"Number of songs in key E: {number_of_songs_in_key(df, 'E')}")
    col_name = get_col_name_user_input(df)
    print(f'Occurences of values in column {col_name}: {count_occurences(df, col_name)}')
    print(f'The most common value in column {col_name} is: {get_most_common_value(df, col_name)}')