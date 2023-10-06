import tkinter
from tkinter import *

def read_csv(filename):
    import pandas as pd

    df = pd.read_csv(filename)
    return df

def count_songs(df):
    return f"-> The number of songs present in the file is {df.shape[0]}"

def count_key(data):
    counts = data['key'].value_counts()['E']

    return f"-> The number of songs with key 'E' is {counts}"

def output(out,out2):
    main = Tk()
    main.title('File I/O')
    

    custom_font = ("Helvetica", 120)
    text_widget = Text(main, width=300, height=1, wrap=WORD,font = custom_font)
    text_widget.insert(INSERT, 'Octoberfest 2023')
    text_widget.config(bg='lightgreen', padx=10, pady=10, wrap=WORD, state=DISABLED)  # Disable editing
    text_widget.pack()

    custom_font = ("Helvetica", 50)
    text_widget = Text(main, width=300, height=1, wrap=WORD,font = custom_font)
    text_widget.insert(INSERT, out)
    text_widget.config(padx=10, pady=10, wrap=WORD, state=DISABLED)  # Disable editing
    text_widget.pack()

    custom_font = ("Helvetica", 50)
    text_widget = Text(main, width=300, height=1, wrap=WORD,font = custom_font)
    text_widget.insert(INSERT, out2)
    text_widget.config(padx=10, pady=10, wrap=WORD, state=DISABLED)  # Disable editing
    text_widget.pack()

    main.mainloop( )



readings = read_csv('spotify-2023.csv')
printthis = count_songs(readings)
printthistoo = count_key(readings)

output(printthis,printthistoo)
