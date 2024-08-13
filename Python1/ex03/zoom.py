import load_image as load
import numpy as np
import PIL.Image as Image, PIL.ImageOps as ImageOps
import subprocess

def zoom(img: str) -> np.ndarray:
    try:
        image = Image.fromarray(load.ft_load(img))
        x, y, h, w = 450, 70, 850, 470
        box = (x, y, h, w)
        cropped = ImageOps.grayscale(image.crop(box))
        cropped.save("cropped.jpeg")
        subprocess.run(["eog", "cropped.jpeg"], stderr=subprocess.DEVNULL)
        return np.array(cropped)
    except Exception as e:
        print(e)
        exit()


def main():
    img = "animal.jpeg"
    img_array = load.ft_load(img)
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)

    cropped = zoom(img)

    print(f"The shape of image after slicing is: {cropped.shape}")
    print(cropped)
    del cropped

if __name__ == "__main__":
    main()