import pandas as pd

df = pd.read_csv('spotify-2023.csv')

def get_songs_count():
  return f"Total number of songs in the file are {df['track_name'].count()}"

def get_songs_with_key_E():
  return f"Total number of songs in the file with key 'E' are {df[df['key'] == 'E']['key'].count()}"

def get_most_common_occurrence(column):
  if column not in df.columns:
    return f"The passed column {column} does not exist in the csv"
  return f"The most common occurrence in the column '{column}' is {df[column].value_counts()[:1].index.to_list()[0]}"

print(get_songs_count())
print(get_songs_with_key_E())

# Can pass any column name to get the most common occurrence of that column.
# If the passed column is not in the csv headers, a generic message will be printed
print(get_most_common_occurrence('key'))