import csv

def read_csv(filename): # Function to read the given csv file
    with open(filename, mode='r') as file:
        contents = list(csv.reader(file))
    return contents

def num_songs(filename): # Number of songs in the file
    contents = read_csv(filename)
    return len(contents[1:])

def key_e_songs(filename): # Number of songs in key E
    contents = read_csv(filename)
    key_index = contents[0].index("key")
    return len([i for i in contents if i[key_index] == 'E'])

def num_values_in_a_field(filename, field, value):
    contents = read_csv(filename)
    if field in contents[0]:
        field_index = contents[0].index(field)
    else:
        return False
    
    field_items = []   
    for i in contents[1:]:
        field_items.append(i[field_index])

    if value not in field_items:
        return 0
    else:
        return field_items.count(value)
