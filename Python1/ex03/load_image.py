
import os
import PIL.Image as Image
import numpy as np


def is_image_file(path) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
            return True, "OK"
    except (IOError, SyntaxError) as err:
            return False, err


def is_accepted_format(path: str, formats: list) -> bool:
    _, ext = os.path.splitext(path)
    return (ext.lower() in formats)


def ft_load(path: str) -> list:
    # if the name is the same as extension
    if  any(path == ext for ext in [".jpeg", ".jpg", ".png"]):
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
    
    return image_array


def main():
    #print(ft_load("test.jpg"))
    ft_load("animal.jpeg")


if __name__ == "__main__":
    main()
    