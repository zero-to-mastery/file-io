import csv
import statistics
import re

# Open CSV file and read rows into a list
with open("spotify-2023.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    rows = list(reader)

# Removes the header row
rows = rows[1:]

# Calculate the average beets per a minute of the songs
bpms = []
for row in rows:
    bpm = row[14]
    if bpm:
        bpm = float(bpm.replace(",", ""))
        bpms.append(bpm)
avg_bpm = statistics.mean(bpms)
print("Average BPM:", avg_bpm)

# Calculate the number of total songs
total_songs = len(rows)
print("Total songs in the CSV file:", total_songs)

# Counts the songs released in 2023
songs_in_2023 = 0
for row in rows:
    date_parts = row[3].split("-")
    year = int(date_parts[0])
    if year == 2023:
        songs_in_2023 += 1

print("Songs released in 2023:", songs_in_2023)

# Display the artist with the most streams
streams_by_artist = {}
for row in rows:
    artist_name = row[1]
    streams_data = row[8]
    streams = int(re.search(r"\d+", streams_data).group())

    if artist_name in streams_by_artist:
        streams_by_artist[artist_name] += streams
    else:
        streams_by_artist[artist_name] = streams

most_streams = max(streams_by_artist.values())
most_streamed_artist = max(streams_by_artist, key=streams_by_artist.get)

print(
    "Most streamed artist:",
    most_streamed_artist,
    "with",
    format(most_streams, ",d"),
    "streams",
)
