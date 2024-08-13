import load_image as load
import numpy as np
import PIL.Image as Image, PIL.ImageOps as ImageOps
import subprocess


def ft_invert(array) -> np.ndarray:
    """ Inverts the color of the image received. """
    return 255 - array

def ft_red(array) -> np.ndarray:
    red_channel = array.copy()
    red_channel[:, :, 1] = 0  # Set green channel to 0
    red_channel[:, :, 2] = 0  # Set blue channel to 0
    return red_channel


def ft_green(array) -> np.ndarray:  
    return array - ft_blue(array) - ft_red(array)


def ft_blue(array) -> np.ndarray:
    blue_channel = array.copy()
    blue_channel[:, :, 0] = 0
    blue_channel[:, :, 1] = 0
    return blue_channel

def ft_grey(array) -> np.ndarray:
     return (array[:,:,0] / 3 + array[:,:,1] / 3 + array[:,:,2] / 3).astype(array.dtype)


""" def rotate(img: str) -> np.ndarray:
    try:
        image = ImageOps.grayscale(Image.fromarray(load.ft_load(img)))

        width, height = image.size

        new_arr = np.zeros((width, height), dtype=np.uint8)
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                new_arr[x, y] = pixel

        Image.fromarray(new_arr).save("rotated.jpeg")
        print()
        subprocess.run(["eog", "rotated.jpeg"], stderr=subprocess.DEVNULL)
        return new_arr
    except Exception as e:
        print(f"An error occurred: {e}")
        exit() """


def main():
    array = load.ft_load("landscape.jpg")
    Image.fromarray(ft_invert(array)).save("invert.jpg")
    Image.fromarray(ft_red(array)).save("red.jpg")
    Image.fromarray(ft_green(array)).save("green.jpg")
    Image.fromarray(ft_blue(array)).save("blue.jpg")
    Image.fromarray(ft_grey(array)).save("grey.jpg")
    

    print(ft_invert.__doc__)

if __name__ == "__main__":
    main()