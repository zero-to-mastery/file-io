import csv
import time

#####################################################################################################
    ##Please include spotify-2023.csv in root directory(atif-dev) for successfully running the code.
#####################################################################################################

print(f'***************************HacktoberFest-2023*****************************')

first_column_values = []

# Open CSV file for reading
with open('spotify-2023.csv', 'r') as file:
    
    reader = csv.reader(file)
    
    # Iterate through the rows of .csv
    for row in reader:
        first_column_values.append(row[0])
    
#################Total Songs#######################
count = 0;
for x in first_column_values:
    if x != "track_name":
        count = count + 1
print(f'Total Songs: {count}')

print(f'**********************************END*************************************')
