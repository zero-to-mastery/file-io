import tkinter as tk
from tkinter import Text, OptionMenu, filedialog
import csv
from modules.count_songs import count_songs
from modules.count_songs_key import count_songs_key
from modules.count_occurrences import count_occurrences

csv_path = "spotify-2023.csv"

default_column_name = "key"
default_key_value = "E"

window = tk.Tk()
window.title("CSV Analysis")

output_text_challenge_one = Text(window, wrap=tk.WORD, width=60, height=3)
output_text_challenge_one.grid(
    row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w"
)

output_text_challenge_two = Text(window, wrap=tk.WORD, width=60, height=3)
output_text_challenge_two.grid(
    row=3, column=2, columnspan=2, padx=10, pady=10, sticky="w"
)

output_text_challenge_three = Text(window, wrap=tk.WORD, width=60, height=3)
output_text_challenge_three.grid(
    row=3, column=4, columnspan=2, padx=10, pady=10, sticky="w"
)

column_name_label_challenge_two = tk.Label(window, text="Column Name:")
column_name_label_challenge_two.grid(row=1, column=2, padx=10, pady=10, sticky="e")

column_name_var_challenge_two = tk.StringVar(window)
column_name_var_challenge_two.set(default_column_name)
column_name_option_menu_challenge2 = OptionMenu(
    window, column_name_var_challenge_two, "key"
)
column_name_option_menu_challenge2.grid(row=1, column=3, padx=10, pady=10)

key_value_label_challenge_two = tk.Label(window, text="Key Value:")
key_value_label_challenge_two.grid(row=2, column=2, padx=10, pady=10, sticky="e")

key_value_entry_challenge_two = tk.Entry(window)
key_value_entry_challenge_two.grid(row=2, column=3, padx=10, pady=10)
key_value_entry_challenge_two.insert(0, default_key_value)


column_name_var_challenge_three = tk.StringVar(window)
column_name_var_challenge_three.set(default_column_name)


def browse_file():
    global csv_path
    csv_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    file_label.config(text=f"Selected CSV file: {csv_path}")
    update_column_options()


file_frame = tk.Frame(window)
file_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

file_label = tk.Label(file_frame, text="Selected CSV file: ")
file_label.grid(row=0, column=1, sticky="w")

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")


def update_column_options():
    global csv_path
    try:
        if csv_path:
            with open(csv_path, "r") as file:
                reader = csv.reader(file)
                columns = next(reader)
                column_name_var_challenge_two.set(default_column_name)
                column_name_option_menu_challenge2["menu"].delete(0, "end")
                for col in columns:
                    column_name_option_menu_challenge2["menu"].add_command(
                        label=col, command=tk._setit(column_name_var_challenge_two, col)
                    )
    except Exception as e:
        print("Error reading CSV file:", e)


def challenge_one():
    song_count = count_songs(csv_path)
    if song_count == -404:
        output_text_challenge_one.delete(1.0, "end")
        output_text_challenge_one.insert("end", "CSV file not found.")
    elif song_count == -400:
        output_text_challenge_one.delete(1.0, "end")
        output_text_challenge_one.insert("end", "Something went wrong.")
    else:
        output_text_challenge_one.delete(1.0, "end")
        output_text_challenge_one.insert("end", f"Number of songs: {song_count}")


def challenge_two():
    column_name = column_name_var_challenge_two.get()
    key_value = key_value_entry_challenge_two.get()
    songs_in_key = count_songs_key(csv_path, column_name, key_value)
    output_text_challenge_two.delete(1.0, "end")
    output_text_challenge_two.insert(
        "end",
        f"Number of songs with the value of {key_value} in the {column_name} column: {songs_in_key}",
    )


def challenge_three():
    column_name = column_name_var_challenge_two.get()
    result = count_occurrences(csv_path, column_name)
    output_text_challenge_three.delete(1.0, "end")
    if result:
        most_common_value, most_common_count = result
        output_text_challenge_three.insert(
            "end",
            f"The most common value in the specified column is '{most_common_value}' with {most_common_count} occurrences.",
        )
    else:
        output_text_challenge_three.insert(
            "end", "An error occurred. Please check the CSV file and column name."
        )


challenge_one_button = tk.Button(window, text="Challenge One", command=challenge_one)
challenge_one_button.grid(row=2, column=0, padx=10, pady=10)

challenge_two_button = tk.Button(window, text="Challenge Two", command=challenge_two)
challenge_two_button.grid(row=2, column=2, padx=10, pady=10)

challenge_three_button = tk.Button(
    window, text="Challenge Three", command=challenge_three
)
challenge_three_button.grid(row=2, column=4, padx=10, pady=10)

window.mainloop()
