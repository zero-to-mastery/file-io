import pandas as pd
import calendar

# read in the csv file using pandas
df = pd.read_csv('spotify-2023.csv')

# count number of rows (songs)
num_rows = len(df.index)
print("Number of songs:", num_rows)

# identify songs with key E
key_e = df[df['key'] == 'E']
num_keys_e = len(key_e.index)
print("Songs in key E:", num_keys_e)

# count unique artists and determine the most common artist
unique_artists = df['artist(s)_name'].nunique()
most_common_artist = df['artist(s)_name'].mode()[0]
print("Number of unique artists:", unique_artists)
print("Most common artist:", most_common_artist)

# detect the year with most releases and number of songs that were released in that year
number_of_songs1 = df['released_year'].nunique()
most_songs_in_year = df['released_year'].mode()[0]
print("Most songs were released in:", most_songs_in_year)
print(f"Number of songs that were released in {most_songs_in_year}:", number_of_songs1)

# detect the month with most releases and number of songs that were released in that month
number_of_songs2 = df['released_month'].nunique()
most_songs_in_month = df['released_month'].mode()[0]
month_name = calendar.month_name[most_songs_in_month]
print("Most songs were released in:", month_name)
print(f"Number of songs that were released in {month_name}:", number_of_songs2)

# detect the day of months with most releases and number of songs that were released in that day
number_of_songs3 = df['released_day'].nunique()
most_songs_in_day = df['released_day'].mode()[0]
print("Most songs were released in day", most_songs_in_day, "of months")
print(f"Number of songs that were released in the day {most_songs_in_day} of months:", number_of_songs3)

# find the song with the highest streams
# because the csv file is faulty in some cells, convert all strings in the `streams` column to numeric values,
# except for strings that contain non-numeric characters and select non null cells
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df = df[df['streams'].notnull()]
max_streams = df['streams'].max()
max_streams_song = df[df['streams'] == max_streams]['track_name'].iloc[0]
print(f"The song with the highest number of streams is {max_streams_song} and has {max_streams} streams \n")

# find the songs with top spotify chart rating
# filter out rows where the in_spotify_charts column is 0 or is a string
df = df[df['in_spotify_charts'].astype(str).str.isdigit() & (df['in_spotify_charts'] != 0)]
top_spotify_rating = df['in_spotify_charts'].min()
songs_with_top_spotify_rating = df[df['in_spotify_charts'] == top_spotify_rating]['track_name']
artist_names = [df.loc[song_index, 'artist(s)_name'].split('& ') for song_index in songs_with_top_spotify_rating.index]
artist_names = [item for sublist in artist_names for item in sublist]
print(f"The {len(songs_with_top_spotify_rating)} songs with the top Spotify chart number ({top_spotify_rating}) are:")
for i in range(len(songs_with_top_spotify_rating)):
    print(f"{songs_with_top_spotify_rating.iloc[i]} by {artist_names[i]}")

# find the song with the highest mean of: total spotify, deezer, apple and shazam chart ranks
# replace non-numeric and NaN values with 0 in the specified columns
numeric_columns = ['in_spotify_charts', 'in_apple_charts', 'in_deezer_charts', 'in_shazam_charts']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)
mean_ranks = df.groupby('track_name')[numeric_columns].mean()
highest_mean_rank = mean_ranks.sum(axis=1).idxmax()
song_info = df[df['track_name'] == highest_mean_rank][['track_name', 'artist(s)_name']].iloc[0]
print(f"\nThe song with the highest mean of total chart ranks is {song_info['track_name']} by {song_info['artist(s)_name']}")

# find the month with total top spotify charts rating and print it with rating number
top_spotify_month = df['in_spotify_charts'].idxmax()
month_name2 = calendar.month_name[df.iloc[top_spotify_month]['released_month']]
print("Month with the highest total spotify charts rating:", month_name2, "with rank", int(df.iloc[top_spotify_month]['in_spotify_charts']))

# find the monthly means of sum of all streams
df['year_month'] = pd.to_datetime(df['released_year'].astype(str) + '-' + df['released_month'].astype(str), format='%Y-%m')
monthly_means = df.groupby('year_month')['streams'].sum()
for month_year, mean_value in monthly_means.items():
    print(f"Month-Year: {month_year.strftime('%Y-%m')}, Monthly Mean: {mean_value}")

# JB-Rockstar
# gokhanbalik8@gmail.com








