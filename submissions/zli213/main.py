import pandas as pd


def try_read_csv(filename, encodings=('utf-8', 'ISO-8859-1', 'windows-1252')):
    for encoding in encodings:
        try:
            return pd.read_csv(filename, encoding=encoding)
        except UnicodeDecodeError:
            pass
    raise UnicodeDecodeError(
        f"Unable to read the file {filename} with any of the provided encodings.")


df = try_read_csv('spotify-2023.csv')


def get_column_names(dataframe):
    return dataframe.columns.to_list()


def get_songs_count():
    return f"Total number of songs in the file are {df['track_name'].count()}"


def get_songs_with_key_E():
    return f"Total number of songs in the file with key 'E' are {df[df['key'] == 'E']['key'].count()}"


def most_common_value_in_column(column_name):
    if column_name not in df.columns:
        return f"The passed column {column_name} does not exist in the csv"
    return f"The most common occurrence in the column '{column_name}' is {df[column_name].value_counts().idxmax()}"


def main():
    print(get_songs_count())
    print(get_songs_with_key_E())

    available_columns = get_column_names(df)
    print("\nAvailable columns are:")
    for column in available_columns:
        print(column)

    while True:  # Keep running until the user decides to exit
        column_name = input(
            "\nPlease enter the column name you'd like to analyze (or type 'exit' to quit): ")

        if column_name.lower() == 'exit':
            print("Goodbye!")
            break  # Exit the loop

        # Check for invalid input
        while column_name not in available_columns:
            print("Invalid input. Please choose from the columns listed above.")
            column_name = input(
                "Please enter the column name you'd like to analyze (or type 'exit' to quit): ")

            if column_name.lower() == 'exit':
                print("Goodbye!")
                return  # Exit the function

        print(most_common_value_in_column(column_name))


if __name__ == "__main__":
    main()

# Navigate to the directory containing this file in your terminal
# Run the following command: python main.py
