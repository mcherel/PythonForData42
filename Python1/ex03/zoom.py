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

    # displaythe image with the x and y scales
    smp = 'viridis' if ((image_array.shape + (0, 0)[:3]) == 3) else 'grey'

    fig, ax = plt.subplots()
    ax.imshow(image_array, extent=[0, x, y, 0], cmap=smp)

    # customize the axes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xticks(np.arange(0, x, 50))
    ax.set_yticks(np.arange(0, y, 50))
    ax.tick_params(axis='both', labelsize=7)

    plt.show()
    return fig


def zoom(img: str) -> np.ndarray:
    try:
        image = Image.fromarray(load.ft_load(img))
        x, y, h, w = 450, 70, 850, 470
        box = (x, y, h, w)
        cropped = ImageOps.grayscale(image.crop(box))
        cropped.save("cropped.jpeg")
        cropped_arr = np.array(cropped)
        show_img(cropped_arr).savefig("with_scale.jpeg")
        plt.show()
        # subprocess.run(["eog", "cropped.jpeg"], stderr=subprocess.DEVNULL)
        return cropped_arr
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
