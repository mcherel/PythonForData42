import load_image as load
import numpy as np
import PIL.Image as Image, PIL.ImageOps as ImageOps
import time

def zoom(img: str) -> list:
    image = ImageOps.grayscale(Image.open(img))
    x = 0
    y = 0
    h = 400
    w = 400
    box = (x, y, h, w)
    print(1)
    crop = image.crop(box)
    crop.show()
    print(2)
    #cv2.waitKey(0) #important
    print(3)
    #cv2.destroyAllWindows() #important
    return np.array(crop)


def main():
    img = "animal.jpeg"
    img_array = load.ft_load(img)
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)
    cropped = zoom(img)
    print(f"The shape of image after slicing is: {cropped.shape}")

if __name__ == "__main__":
    main()