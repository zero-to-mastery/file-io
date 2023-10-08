#my GitHub: https://github.com/dKouela

import subprocess
import pandas as pd

# Function to check and install Pandas
def check_and_install_pandas():
    try:
        import pandas as pd 
        print('\nYou have the necessary library to start working with the file.')
        print('Reading the CSV file .............\n')
    except ImportError:
        print('Pandas is not installed. We will install it now. Please wait for the installation to complete.')
        try:
            subprocess.call(['pip', 'install', 'pandas'])
            import pandas as pd
            print('Pandas has been successfully installed.')
        except Exception as e:
            print(f'Pandas installation failed with error: {e}. Please install it manually using "pip install pandas".')
        print('\n')

# Function to read and count songs in the CSV file
def count_songs_in_csv():
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv('./data.csv')
        
        # Get the number of rows, which represents the number of songs
        num_songs = len(df)
        
        return num_songs
    except Exception as e:
        print(f'Error while reading the CSV file: {e}')
        return None

# Function to find the most common value in a specified column
def most_common_value_in_column(file_path, column_name):
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Using the value_counts() function to count occurrences of each unique value in the specified column
        value_counts = df[column_name].value_counts()
        
        # Find the most common value (first value in the sorted counts)
        most_common_value = value_counts.index[0]
        
        return most_common_value
    except Exception as e:
        print(f'Error while reading the CSV file: {e}')
        return None

# Main part of the script
if __name__ == "__main__":
   # print('\nYou have the necessary library to start working with the file.')
    #print('Reading the CSV file .............\n')
    
    # Call the function to check and install Pandas
    check_and_install_pandas()

    # Specifying the path to CSV file and the column name
    csv_file_path = './data.csv'  
    column_name = 'track_name' 

    # Call the function to count songs
    num_songs = count_songs_in_csv()
    
    # Print the result
    if num_songs is not None:
        print(f'The number of songs in the file is: {num_songs}\n')

    # Call the function to find the most common value in the specified column
    common_artist = most_common_value_in_column(csv_file_path, column_name)

    # Print the result
    if common_artist is not None:
        print(f'The most common {column_name} is: {common_artist}\n')
