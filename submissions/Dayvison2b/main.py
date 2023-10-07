import csv
from collections import Counter



def load_csv_data(path, filename):
    with open(path + filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        return list(csvreader), fields

def count_songs(data):
    songsCount = len(data)
    return songsCount
    
def count_songs_in_keyE(data, fields):
    key_index = fields.index('key')
    songsInKeyE = sum(1 for row in data if row[key_index] == 'E')
    return songsInKeyE

def get_most_common_value(data, fields, column_name):
    indexToAnalyze = fields.index(column_name)
    columnsToAnalyze = [row[indexToAnalyze] for row in data]
    mostCommonValue = max(Counter(columnsToAnalyze).values())
    return mostCommonValue

# Exemplo de uso:
path = '../../' 
filename = 'spotify-2023.csv'

data, fields = load_csv_data(path, filename)
songsCount = count_songs(data)
songsInKeyE = count_songs_in_keyE(data, fields)
mostCommonValue = get_most_common_value(data, fields, 'artist(s)_name')

print(f'O número de músicas é: {songsCount}')
print(f'O número de músicas em chave "E" é: {songsInKeyE}')
print(f'O valor mais comum na coluna "artist(s)_name" é: {mostCommonValue}')