import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Import spotify csv file and make a data frame
df = pd.read_csv("spotify-2023.csv")


def number_of_songs():
    """Returns the number of songs in the dataset"""
    return f"There are {len(df)} songs in the dataset."


def key_occurence(key):
    """Returns the number of times a key occurs in the dataset"""
    return f"{key} occurs {len(df[df['key'] == key])} times in the dataset."


def top_artist(df):
    artists = df["artist(s)_name"].value_counts()

    top_artists = artists.head(10)
    # Create a horizontal bar plot
    sns.barplot(x=top_artists.values, y=top_artists.index)

    # Label the axes
    plt.title("Top 10 Artists in the Spotify Dataset")
    plt.xlabel("Number of Songs")
    plt.ylabel("Artist Name")

    # Display the plot
    plt.show()

    return f"The top artist in the dataset is {top_artists.index[0]} with {top_artists.values[0]} songs."


if __name__ == "__main__":
    #Challenge 1
    print(number_of_songs())
    #Challenge 2
    print(key_occurence("E"))
    #Challenge 3
    print(top_artist(df))