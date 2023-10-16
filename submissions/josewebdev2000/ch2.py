# ZTM 2023 Hacktoberfest
# Solution for the second challenge of File/IO
# Find the number of songs in the key of E

# Imports
import pandas as pd

def main():
    """Run the program as a whole."""
    
    # Store the file name in a local variable
    csv_to_read = "spotify-2023.csv"
    
    # Read CSV data into a Pandas DataFrame
    spotify_data = pd.read_csv(csv_to_read)
    
    # Drop NaN values
    spotify_data = spotify_data.dropna()
    
    # Grab songs that have E as their key
    e_key_songs = spotify_data[spotify_data["key"] == "E"]
    
    # Grab the length of the Pandas DateFrame of songs in key of E
    num_e_key_songs = e_key_songs.shape[0]
    
    # Show it to the user
    print(f"In {csv_to_read} there are {num_e_key_songs} songs in key of E.")
    
if __name__ == "__main__":
    """Only run if the code was not imported."""
    main()