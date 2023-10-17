import pandas as pd
import matplotlib.pyplot as plt

class SpotifyDataAnalyzer:

    def __init__(self, file_name='spotify-2023.csv'):
        # Load the data from the given CSV file using pandas
        self.data = pd.read_csv(file_name, encoding='latin-1')

    def number_of_songs(self):
        """Return the total number of songs in the dataset."""
        return self.data.shape[0]

    def common_artist(self):
        """Return the list of most common artists in the dataset."""
        return self.data['artist(s)_name'].mode().tolist()

    def visualize_bpm_distribution(self):
        """Plot the distribution of song tempos (BPM) using a histogram."""
        plt.hist(self.data['bpm'], bins=10, edgecolor='k')
        plt.title('BPM Distribution')
        plt.xlabel('BPM (Tempo)')
        plt.ylabel('Frequency')
        plt.show()

if __name__ == "__main__":
    analyzer = SpotifyDataAnalyzer()

    print(f"The total number of songs in the playlist: {analyzer.number_of_songs()}")
    print(f"The most common artists occuring in the playlist: {analyzer.common_artist()}")
    analyzer.visualize_bpm_distribution()
