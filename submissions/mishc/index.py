import csv, sys,os
from delete_double_rows import delete_double_rows 
import analyse as anal


try:        
    with open('spotify-2023.csv', 'r', encoding='ISO-8859-1') as file:
        csv_reader = csv.reader(file)
        unique_lines=delete_double_rows(csv_reader)
    with open('spotify-2023.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(unique_lines)
    with open('spotify-2023.csv', 'r', encoding='ISO-8859-1') as file: 
        csv_reader = csv.reader(file)  
        anal.analysis(csv_reader)
    

except FileNotFoundError:
    print("File not found")
except csv.Error as e:
    print(f"CSV Error: {type(e).__name__} - {str(e)}")
except Exception as e:
    print(f"An error occurred: {type(e).__name__} - {str(e)}")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)

