from PIL import Image
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import argparse


# NTSC formula
def grayscale_NTSC(img):
    np_img = np.array(img)
    gray_image = 0.299 * np_img[:, :, 0] + 0.587 * np_img[:, :, 1] + 0.114 * np_img[:, :, 2]
    return Image.fromarray(np.uint8(gray_image))

# Averaging method
def grayscale_average(img):
    np_img = np.array(img)
    gray_image = np.mean(np_img, axis=2)
    return Image.fromarray(np.uint8(gray_image))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing images.')
    parser.add_argument('-i', '--image', type=str, default='input_images/image_0.jpeg', help='Image path')

    # Parsing parameters.
    args = parser.parse_args()
    image_path = f"input_images/{args.image}"

    image = Image.open(image_path)
    
    image_grayscale_NTSC = grayscale_NTSC(image)
    image_grayscale_average = grayscale_average(image)

    image.show()
    image_grayscale_NTSC.show()
    image_grayscale_average.show()