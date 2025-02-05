import pandas as pd

# Load the CSV file into a DataFrame with specified encoding
file_path = 'spotify-2023.csv'
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file_path, encoding='latin1')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Challenge 1: Identify the number of songs in the file
def count_songs(df):
    return len(df)

# Challenge 2: Identify the number of songs in the key of E
def count_songs_in_key_e(df):
    return len(df[df['key'] == 'E'])

# Challenge 3: Count the occurrences of values in a specified column and determine the most common value
def most_common_value(df, column_name):
    return df[column_name].value_counts().idxmax(), df[column_name].value_counts().max()

# Main function to run the analysis
def main():
    # Challenge 1
    num_songs = count_songs(df)
    print(f"Number of songs in the file: {num_songs}")

    # Challenge 2
    num_songs_key_e = count_songs_in_key_e(df)
    print(f"Number of songs in the key of E: {num_songs_key_e}")

    # Challenge 3
    column_name = 'artist(s)_name'  # Example column, you can change this to any column you're interested in
    most_common, count = most_common_value(df, column_name)
    print(f"The most common value in the '{column_name}' column is '{most_common}' with {count} occurrences.")

if __name__ == "__main__":
    main()