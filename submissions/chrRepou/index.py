import csv
from pathlib import Path

current_directory = str(Path.cwd()) + "\\file-io\\spotify-2023.csv"
songs = 0;
E_songs = 0;
with open(current_directory, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        songs += 1;
        if row[0][0].capitalize() == 'E':
            E_songs += 1;


print("total songs:", songs);
print("total songs that start with E:", E_songs);
