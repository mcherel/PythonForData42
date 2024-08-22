import csv
import numpy as np
def load(path: str) -> list:
    """"""
    dataset = []
    with open (path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        stripped_rows = list([[field.strip() for field in row] for row in reader])
        for row in stripped_rows:
            dataset.append(row)

    print(f"Loading dataset of dimensions {np.array(dataset).shape}")
    return np.array(dataset)
