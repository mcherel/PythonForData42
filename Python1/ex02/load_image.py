""" from PIL import Image

filename = "landscape.jpg"
img = Image.open(filename)
img.show() """

import cv2

image = cv2.imread('landscape.jpg')
if image is None:
    print("Error: unable to loade image.")
else:
    cv2.imshow('Landscape', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()