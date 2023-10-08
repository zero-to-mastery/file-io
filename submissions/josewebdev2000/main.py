# ZTM 2023 Hacktoberfest
# Solution for the first challenge of File/IO
# Find the number of songs in the file

# Imports
import pandas as pd

def main():
    """Run the program as a whole."""
    
    # Store the file name in a local variable
    csv_to_read = "spotify-2023.csv"
    
    # Read CSV data into a Pandas DataFrame
    spotify_data = pd.read_csv(csv_to_read)
    
    # Grab the DataSeries from the column track_name
    songs = spotify_data["track_name"]
    
    # Drop NaN values from the column in case there are any
    songs = songs.dropna()
    
    # Grab the number of songs by getting the length of the songs DataSeries
    num_songs = len(songs)
    
    # Show the number of songs to the user
    print(f"The file {csv_to_read} contains {num_songs} songs.")
    

if __name__ == "__main__":
    """Only run if the code was not imported."""
    main()