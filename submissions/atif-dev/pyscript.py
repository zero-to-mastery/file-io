import csv
import time

#####################################################################################################
    ##Please include spotify-2023.csv in root directory(atif-dev) for successfully running the code.
#####################################################################################################

# ANSI escape codes for text styling
BOLD = "\033[1m"
RESET = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLINK = "\033[5m"

print(f'{BLINK}{YELLOW}***************************HacktoberFest-2023*****************************{RESET}')

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

    #---Animation---
sum = '.'
for i in range(3, 0, -1):
    print(f'{CYAN}Initializing Hacking{sum}{RESET}', end='\r')
    sum = sum + '.';
    time.sleep(1)

print(f'\n')

for i in range(3, 0, -1):
    if(i == 1):
        print(f'{CYAN}Hacking in:{RESET} {i}...\n')
        time.sleep(1)
        break;
    print(f'{CYAN}Hacking in:{RESET} {i}')

    time.sleep(1)

#################Total Songs#######################
print(f'************************************************')

count = 0;
for x in first_column_values:
    if x != "track_name":
        count = count + 1
print(f'{BOLD}Total Songs:{RESET} {count}')

#################Songs in  Key of E################
print(f'************************************************')

ErowCount = 0;
for keyValue in key_column_values:
    if keyValue != "key":
        if keyValue == "E":
            ErowCount = ErowCount + 1
print(f'{BOLD}Total Songs in key of E:{RESET} {ErowCount}')

################Occurences of Values and most Common value###############
print(f'************************************************')

print(f'{BOLD}Occurences of values in a specified column:{RESET}\n')

print(f'|||{BOLD} Specified Column Name:{RESET} {specified_column_values[0]} |||\n')

for sValue in specified_column_values:
    if(sValue == "artist(s)_name"):
        specifiedColumnName = sValue;
    if sValue != "artist(s)_name":
        print(f'{BOLD}>{sValue}:{RESET} occured {specified_column_values.count(sValue)} times(s).')

print(f'-------------------------------------------------------------------------')
mostCommonValue = max(set(specified_column_values), key = specified_column_values.count)
print(f'{BOLD}>{mostCommonValue} is the most common value in specified column {specifiedColumnName}{RESET}.');
print(f'{BLINK}{YELLOW}{BOLD}**********************************END********************************😎😇{RESET}')
