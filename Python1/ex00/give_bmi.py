import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI (Body Mass Index) for a list of given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[float]: List of corresponding BMI values.

    Raises:
        ValueError: If the lists of heights and weights are not of the same length.
        TypeError: If the values in the lists are not integers or floats.
    """
    try:
        len_err = "The lists of heights and weights must have the same length."
        if not len(height) == len(weight):
            raise ValueError(len_err)
        type_err = "All values in the lists must be integers or floats."
        if not all(isinstance(i, (int, float)) for i in height):
            raise TypeError(type_err)
        if not all(isinstance(i, (int, float)) for i in weight):
            raise TypeError(type_err)
            
        bmi = np.array(weight) / np.array(height) ** 2
        return bmi.tolist()
    except (ValueError, TypeError) as e:
        print ("Error:", e)
        exit()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply an upper limit to BMI values to determine if they exceed this limit.

    Args:
        bmi (list[float]): List of BMI values.
        limit (int): BMI limit value.

    Returns:
        list[bool]: List indicating for each BMI value whether it exceeds the limit (True) or not (False).

    Raises:
        TypeError: If the value of the limit is not integer.
        TypeError: If the values in the BMI list are not integers or floats.
    """
    try:
        if not isinstance(limit, (int)):
            raise TypeError("Limit must be an integer")
        type_err = "All values in the lists must be integers or floats."
        if not all(isinstance(i, (int, float)) for i in bmi):
            raise TypeError(type_err)
        return (np.array(bmi) > limit).tolist()
    except (TypeError) as e:
        print ("Error:", e)
        exit()


def main():
    """
    Main function to test the give_bmi and apply_limit functions.
    """
    heights = [1.75, 1.8, 1.65, 1.1, 1.5, 1.75]
    weights = [65, 75, 50, 20, 50, 88]
    bmi = give_bmi(heights, weights)
    print("Calculated BMI:", bmi)

    limit = 25
    bmi_above_limit = apply_limit(bmi, limit)
    print(f"BMI above the limit of {limit}:", bmi_above_limit)

if __name__ == "__main__":
    main()