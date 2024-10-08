import csv
import numpy as np
import os


def is_accepted_format(path: str, formats: list) -> bool:
    """Checks if the format is in the given list of formats.
    Returns: bool
    """
    _, ext = os.path.splitext(path)
    return (ext.lower() in formats)


def load(file_path: str) -> np.array:
    """
    Takes an str pas as parameter
    Loads csv file counts data lines.
    Returns: NumPy array including the header
    """
    if not os.path.exists(file_path):
        print(f"Error: No such file or directory: '{file_path}'")
        exit()
    # if the name is the same as extension
    if file_path == ".csv":
        print("Error: wrong file name")
        exit()
    # if the format of the image is not supported
    if not is_accepted_format(file_path, [".csv"]):
        print("Error: wrong extention")
        exit()
    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=','))
        # if cannot genetate a data table form the given file
        if not reader:
            print("Error: the file is empty")
            exit()
        # if the data table is too small
        if len(reader) < 2 or len(reader[0]) < 2:
            print("Error: there is no enough data in the file (min 2 x 2)")
            exit()
        len_err = "All lists in file must have the same length."
        # if the data table is not rectanngular
        if not all(len(reader[0]) == len(i) for i in reader):
            print(f"Error: {len_err}")
            exit()
        stripped_rows = list([[field.strip()
                             for field in row]
                             for row in reader[1:]])
        print(f"Loading dataset of dimensions {np.array(stripped_rows).shape}")
        return np.array(reader)


def main():
    load("")
    print(load("five.csv"))
    print("later")
    print(load("four.csv"))
    load("one.csv")
    load("empty.csv")
    load(".csv")
    load("hello.txt")


if __name__ == "__main__":
    main()
