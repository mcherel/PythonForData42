import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ Takes as parameters a 2D array, prints its shape, 
    and returns a truncated version of the array 
    based on the provided start and end arguments.
    """
    try:
        if not isinstance(start, (int)):
            raise TypeError("start must be an integer")
        if not isinstance(end, (int)):
            raise TypeError("start must be an integer")
        if type(family) is not list:
            raise TypeError("family has be a list")
        len_err = "All elements in 'family' must be lists."
        if not all(type(i) is list for i in family):
            raise TypeError(len_err)
        len_err = "All lists in 'family' must have the same length."
        if not all(len(family[0]) == len(i) for i in family):
            raise ValueError(len_err)
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        subarr = arr[start:end, 0:len(family[0])]
        print(f"My new shape is : {subarr.shape}")
        return subarr.tolist()
    except (TypeError, ValueError) as e:
        print ("Error:", e)
        exit()


def main():
    """
    Main function to test the give_bmi and apply_limit functions.
    """
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()
