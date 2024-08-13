import load_image as load
import numpy as np
import PIL.Image as Image, PIL.ImageOps as ImageOps
import subprocess

def zoom(img: str) -> list:
    try:
        image = ImageOps.grayscale(Image.fromarray(load.ft_load(img)))
        x = 450
        y = 70
        h = 850
        w = 470
        box = (x, y, h, w)
        cropped = ImageOps.grayscale(image.crop(box))
        cropped.save("crop.jpeg")
        #crop.show()
        # Execute the eog command with error output redirected to /dev/null
        subprocess.run(["eog", "crop.jpeg"], stderr=subprocess.DEVNULL)
        #cv2.waitKey(0) #important
        #cv2.destroyAllWindows() #important
        return np.array(cropped)
    except:
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