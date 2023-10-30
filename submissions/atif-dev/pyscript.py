import csv
import time

#####################################################################################################
    ##Please include spotify-2023.csv in root directory(atif-dev) for successfully running the code.
#####################################################################################################

print(f'***************************HacktoberFest-2023*****************************')

first_column_values = []
key_column_values = []
specified_column_values =  []

# Open CSV file for reading
with open('spotify-2023.csv', 'r') as file:
    
    reader = csv.reader(file)
    
    # Iterate through the rows of .csv
    for row in reader:
        first_column_values.append(row[0])
        key_column_values.append(row[15])
        specified_column_values.append(row[1]) # have sleected second column as specified column.
    
#################Total Songs#######################
count = 0;
for x in first_column_values:
    if x != "track_name":
        count = count + 1
print(f'Total Songs: {count}')

print(f'************************************************')
#################Songs in  Key of E################
ErowCount = 0;
for keyValue in key_column_values:
    if keyValue != "key":
        if keyValue == "E":
            ErowCount = ErowCount + 1
print(f'Total Songs in key of E: {ErowCount}')

################Occurences of Values###############
print(f'************************************************')

print(f'Occurences of values in a specified column:\n')

print(f'||| Specified Column Name: {specified_column_values[0]} |||\n')

for sValue in specified_column_values:
    if(sValue == "artist(s)_name"):
        specifiedColumnName = sValue;
    if sValue != "artist(s)_name":
        print(f'>{sValue}: occured {specified_column_values.count(sValue)} times(s).')

print(f'**********************************END*************************************')


