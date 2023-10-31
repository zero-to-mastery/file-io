import itertools
def delete_double_rows(csvObject):

    unique_lines = []
    encountered_lines = set()

    for row in csvObject:
        row_tuple = tuple(row)

        if row_tuple not in encountered_lines:
            unique_lines.append(row)

            encountered_lines.add(row_tuple)
    return unique_lines