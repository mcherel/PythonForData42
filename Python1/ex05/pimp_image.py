import load_image as load
import numpy as np
import PIL.Image as Image, PIL.ImageOps as ImageOps
import subprocess


def ft_invert(array: np.array) -> np.array:
    """ Inverts the color of the image received. """
    invert = (255 - array).astype(array.dtype)
    Image.fromarray(invert).save("invert.jpg")
    print(f"The shape of image is: {invert.shape}")
    print(load.ft_load("invert.jpg"))
    return invert

def ft_red(array: np.array) -> np.array:
    """ Only red color is left. """
    red = (array * [1, 0, 0]).astype(array.dtype)
    Image.fromarray(red).save("red.jpg")
    print(f"The shape of image is: {red.shape}")
    print(load.ft_load("red.jpg"))
    return red


def ft_green(array: np.array) -> np.array:
    """ Only green color is left. """
    green = np.zeros_like(array)
    red_and_blue = ((array[:,:,0] - array[:,:,1]) - array[:,:,2])
    green[:, :, 1] = array[:, :, 1] - red_and_blue
    green = np.clip(green, 0, 255)
    Image.fromarray(green).save("green.jpg")
    print(33333333333333333333333333333333333333)
    print(f"The shape of image is: {green.shape}")
    print(load.ft_load("green.jpg"))
    return green


def ft_blue(array: np.array) -> np.array:
    """ Only blue color is left. """
    blue_channel = array.copy()
    blue_channel[:, :, 0] = 0
    blue_channel[:, :, 1] = 0
    print(4444444444444444444444)
    Image.fromarray(blue_channel).save("blue.jpg")
    print(f"The shape of image is: {blue_channel.shape}")
    print(load.ft_load("blue.jpg"))
    return blue_channel

def ft_grey(array: np.array) -> np.array:
     """ Only grayscale is left. """
     grey = (array[:,:,0] / 3 + array[:,:,1] / 3 + array[:,:,2] / 3).astype(array.dtype)
     Image.fromarray(grey).save("grey.jpg")
     print(f"The shape of image is: {grey.shape}")
     print(load.ft_load("grey.jpg"))
     return grey



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