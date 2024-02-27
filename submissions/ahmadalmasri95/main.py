# Let's import the pandas library first to deal with csv file
import pandas
# Read the csv file using pandas and convert it to DataFrame
df = pandas.read_csv('spotify-2023.csv',encoding_errors='replace')
# Let's do some analysis on the data we've got
total_songs = len(df)
num_songs_in_E_key = len(df[df[key]=='E'])
release_years_counts = df['released_year'].nunique()
max_year_of_releases = df['released_year'].max()
# Displaying our simple analysis
print(f'Total songs are :{total_songs}')
print(f'The number of songs in the key of E is :{num_songs_in_E_key}')
print(f'The number of release years are :{release_years_counts}')
print(f'The most year of released songs is :{max_year_of_releases}')