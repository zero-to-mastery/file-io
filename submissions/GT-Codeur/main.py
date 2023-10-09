import csv
from collections import Counter

# csv filename
filename = 'spotify-2023.csv'

# Reading the csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Let's extract fields from the file
    fields = next(csvreader)

    # Let's extract the rows from the file
    # and count occurrences of most common value in a column
    key_index = fields.index('key')
    columnToAnalyze = 'artist(s)_name'
    indexToAnalyze = fields.index(columnToAnalyze)
    songsInKeyE = 0
    rows = []
    columnsToAnalyze = []
    for i, row in enumerate(csvreader):
        # Get songs in key E
        if row[key_index] == 'E':
            songsInKeyE += 1
        rows.append(row)
        #Create column of value for the specified column
        columnsToAnalyze.append(row[indexToAnalyze])

    mostCommonValue = max(Counter(columnsToAnalyze).values())


# Outputs:
print(f'Number of songs in the file: {len(rows)}')
print(f'Number of songs in the key of E: {songsInKeyE}')
print(f'Most common value: {mostCommonValue}')

