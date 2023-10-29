import csv
from collections import Counter

# csv filename
filename = 'spotify-2023.csv'

# Read the csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Extract fields from the file
    fields = next(csvreader)

    # Extract the rows from the file
    # and count occurrences of most common value in a column
    rows = []
    columnsToAnalyze = []
    for row in csvreader:
        rows.append(row)
        columnsToAnalyze.append(row[fields.index('artist(s)_name')])

    # Get songs in key E
    songsInKeyE = len([row for row in rows if row[fields.index('key')] == 'E'])

    # Find the most common value in the column
    mostCommonValue = max(Counter(columnsToAnalyze).values())

# Outputs:
print(f'Number of songs in the file: {len(rows)}')
print(f'Number of songs in the key of E: {songsInKeyE}')
print(f'Most common value: {mostCommonValue}')
