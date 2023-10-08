import csv

with open("./spotify-2023.csv", "r") as spotify_file:
  spotify_data = csv.DictReader(spotify_file)
  spotify_data = list(spotify_data)

  length_of_spotify_data = len(spotify_data)
  
  # We'll count the number of rows where "key" is equal to "E"
  countOfE = 0
  
  # We'll also count the number of unique artists by creating an empty dictionary to house each artist with their count
  unique_artists = {}
  
  for row in spotify_data:
    if row.get("key") == "E":
      countOfE += 1
    artist = row.get("artist(s)_name")
    if artist not in unique_artists:
      # If the artist is not yet in our dictionary, add it with a count of 1
      unique_artists[artist] = 1
    else:
      # If the artist IS in our dictionary, increment it
      unique_artists[artist] += 1

  # Determine most popular artist
  most_popular_artist = max(unique_artists, key=unique_artists.get)
  count_of_most_popular = unique_artists[most_popular_artist]
  
print("There are " + str(length_of_spotify_data) + " songs in the CSV file.")
print(str(countOfE) + " of those songs are in the key of 'E'.")
print("The most popular artist is '" + most_popular_artist + "' with " + str(count_of_most_popular) + " songs.")