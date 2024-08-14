
import os
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt

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

    y, x, p = image_array.shape
    print(x)
    print(y)
    print(p)

    # displaythe image with the x and y scales

    fig, ax = plt.subplots()
    ax.imshow(image_array, extent=[0, x, y, 0])
    #ax.invert_yaxis()

    #customize the axes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xticks(np.arange(0, x+1, 50))
    ax.set_yticks(np.arange(0, y+1, 50))
    ax.tick_params(axis='both', labelsize=7)

    plt.show()
    
    #print(f"The shape of image is: {image_array.shape}")
    #time.sleep(5)

    #del image
    #first = image_array[0,0:3]
    #last = np.squeeze(image_array[-1:,-4:-1])
    #return first
    #return np.vstack([[first, last]])
    return image_array


def main():
    #print(ft_load("test.jpg"))
    ft_load("animal.jpeg")


if __name__ == "__main__":
    main()