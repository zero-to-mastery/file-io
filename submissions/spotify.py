import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('spotify-2023.csv',encoding='latin-1')

def number_of_songs(data):
    return data.shape[0]

def common_artist(data):
    return data['artist(s)_name'].mode().tolist()

def vis_bpm(data):
    plt.hist(data['bpm'], bins=10, edgecolor='k')
    plt.title('BPM Distribution')
    plt.xlabel('BPM (Tempo)')
    plt.ylabel('Frequency')
    plt.show()

print(f"The total number of songs in the playlist: {number_of_songs(data)}")
print(f"The most common artists occuring in the playlist: {common_artist(data)}")
vis_bpm(data)