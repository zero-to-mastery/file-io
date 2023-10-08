import pandas as pd

df = pd.read_csv("./spotify-2023.csv") # df = dataframe
rows = len(df)

print(f"Number of songs: {rows}") # number of songs

def countSongsInE(df):
    songs = 0
    for i in range(len(df)):
        E = df.iloc[i]['key']
        if pd.notna(E) and 'E' in E:
            songs += 1
    return songs

def mostCommonInCol(df, column):
    valueCount = df[column].value_counts()
    common = valueCount.index[0]
    return common

Ecount = countSongsInE(df)
print(f"Number of songs in the key of E: {Ecount}") # number of songs in E

while True: # most common value in a specified column
    column = input("Which column would you like to know the most common value in? Type 'exit' to exit the program. ")
    
    if column == 'exit':
        break
    
    if column in df.columns:
        commonValue = mostCommonInCol(df, column)
        print(f"The most common value in column '{column}' is: {commonValue}")
        break
    else:
        print(f"Column '{column}' was not found in this file.")
