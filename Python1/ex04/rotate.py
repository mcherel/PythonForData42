import load_image as load
import numpy as np
import PIL.Image as Image
import PIL.ImageOps as ImageOps
import matplotlib.pyplot as plt
# import subprocess


def show_img(image_array: np.array):
    print(image_array.shape)
    y, x = image_array.shape

    print(x)
    print(y)
    print(image_array.shape)

    # displaythe image with the x and y scales
    smp = 'viridis' if ((image_array.shape + (0, 0)[:3]) == 3) else 'grey'
    print(smp)
    fig, ax = plt.subplots()
    print(fig)
    print("hello")
    ax.imshow(image_array, extent=[0, x, y, 0], cmap=smp)
    plt.show()
    print("hi")

    # customize the axes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xticks(np.arange(0, x, 50))
    ax.set_yticks(np.arange(0, y, 50))
    ax.tick_params(axis='both', labelsize=7)

    return fig


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
        show_img(np.array(new_arr)).savefig("with_scale.jpeg")
        # subprocess.run(["eog", "rotated.jpeg"], stderr=subprocess.DEVNULL)
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
