# ZTM 2023 Hacktoberfest
# Solution for the third challenge of File/IO
# Grab a specific column from the dataset and find the most common value

# MY SPECIAL ADDITION
# I will grab a random column to work on it

# Imports
import pandas as pd
import random

def main():
    """Run the program as a whole."""
    
    # Store the file name in a local variable
    csv_to_read = "spotify-2023.csv"
    
    # Read CSV data into a Pandas DataFrame
    spotify_data = pd.read_csv(csv_to_read)
    
    # Drop NaN values
    spotify_data = spotify_data.dropna()
    
    # Grab column to work with
    chosen_column = get_chosen_random_column(spotify_data)
    
    # Grab mode and repetitions
    mode_n_reps = get_mode_n_reps(spotify_data[chosen_column])
    
    # Show the results to the user
    print(f"The most common value for the column {chosen_column} is {mode_n_reps['mode']}; this value appears {mode_n_reps['reps']} times in the dataset.")

def get_chosen_random_column(pandas_df):
    """Return a random column from the list of column names of a Pandas DataFrame."""
    
    return random.choice(pandas_df.columns)
    
def get_mode_n_reps(pandas_ds):
    """Return the mode of a pandas DataSeries along with the number of times it repeats."""
    
    # Grab the most common value
    mode_value = pandas_ds.mode().values[0]
    
    # Grab the number of repetitions of this mode
    mode_reps = pandas_ds.value_counts()[mode_value]
    
    # Return a dict for both the mode and the number of times it repeats
    return {
        "mode": mode_value,
        "reps": mode_reps
    }
    

if __name__ == "__main__":
    """Only run if the code was not imported."""
    main()