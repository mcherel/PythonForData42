import load_image as load
import numpy as np
import PIL.Image as Image, PIL.ImageOps as ImageOps
import subprocess

def rotate(img: str) -> np.ndarray:
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
        exit()


def main():
    img = "cropped.jpeg"
    img_array = ImageOps.grayscale(Image.fromarray(load.ft_load(img)))
    print(f"The shape of image is: {np.array(img_array).shape}")
    print(np.array(img_array))
    irotate = rotate(img)
    print(f"The shape of image after Transpose is: {irotate.shape}")
    print(irotate)
    del irotate

if __name__ == "__main__":
    main()