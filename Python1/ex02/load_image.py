
import os
import PIL.Image as Image
import numpy as np


def is_image_file(path) -> bool:
    """Checks if it's an image file.
    Returns: bool + error message if False
    """
    try:
        with Image.open(path) as img:
            img.verify()
            return True, "OK"
    except (IOError, SyntaxError) as err:
        return False, err


def is_accepted_format(path: str, formats: list) -> bool:
    """Checks if the format is in the given list of formats.
    Returns: bool
    """
    _, ext = os.path.splitext(path)
    return (ext.lower() in formats)


def ft_load(path: str) -> list:
    """Opens image after all the checks
    Returns: np.array
    """
    # if the name is the same as extension
    if any(path == ext for ext in [".jpeg", ".jpg", ".png"]):
        print("Error: wrong file name")
        exit()
    # if the file is not an image
    if not is_image_file(path)[0]:
        print("Error:", is_image_file(path)[1])
        exit()
    # if the format of the image is not supported
    if not is_accepted_format(path, [".jpeg", ".jpg", ".png"]):
        print("Error: wrong extention")
        exit()

    image = Image.open(path)

    if image is None:
        print("Error: unable to loade image.")
        exit()

    image_rgb = image.convert('RGB')
    image_array = np.array(image_rgb)

    print(f"The shape of image is: {image_array.shape}")
    return image_array


def main():
    ft_load("landscape.jpg")


if __name__ == "__main__":
    main()
