import load_image as load
import numpy as np
import cv2
import time

def zoom(img: str) -> list:
    image = cv2.imread(img, 0)
    x = 400
    y = 100
    h = 400
    w = 400
    crop = image[y:y+h, x:x+w]
    print(1)
    cv2.imshow('Cropped image', crop)
    print(2)
    cv2.waitKey(0) #important
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