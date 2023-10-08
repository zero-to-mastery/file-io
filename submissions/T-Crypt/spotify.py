import pandas as pd

def count_songs_in_key_of_e(dataframe):
    key_of_e_songs = dataframe[dataframe['key'] == 'E']
    return len(key_of_e_songs)

def main(csv_file_path):
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

    total_songs = len(df)
    print(f'Total number of songs: {total_songs}')
  
    songs_in_key_of_e = count_songs_in_key_of_e(df)
    print(f'Number of songs in the key of E: {songs_in_key_of_e}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_csv_file>")
    else:
        csv_file_path = sys.argv[1]
        main(csv_file_path)
