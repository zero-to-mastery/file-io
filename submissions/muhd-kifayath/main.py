import pandas as pd
df = pd.read_csv("./spotify-2023.csv")

# Challenge 1: Identify the number of songs in the file
print("Total number of songs:", len(df['track_name']))
print("Number of unique songs:", len(pd.unique(df['track_name'])))

# Challenge 2: Identify the number of songs in the key of E
print("The number of songs in the key of E:", len(df[df['key']=='E']))

# Challenge 3: Count the occurrences of artist names and find the most common value
artists = df['artist(s)_name'].mode().to_list()
print("Common artist(s):")
for i in artists:
    print(i)

