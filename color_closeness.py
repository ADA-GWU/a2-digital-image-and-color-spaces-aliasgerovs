import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
from skimage.color import deltaE_cie76

picked_color = []

def pick_color(event, image):
    global picked_color
    x, y = event.xdata, event.ydata
    if x is not None and y is not None:
        x, y = int(x), int(y)
        picked_color = image[y, x].tolist()
        print(f"Picked Color: {picked_color}")
        plt.close()

def display_image(image):
    fig, ax = plt.subplots()
    ax.imshow(image)
    return fig

def color_picker(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    fig = display_image(image)
    fig.canvas.mpl_connect('button_press_event', lambda event: pick_color(event, image))
    plt.show()

def highlight_similar_colors(image, picked_color, threshold=10):
    picked_color_rgb = np.array([picked_color], dtype=np.uint8).reshape(1, 1, 3)
    picked_color_lab = cv2.cvtColor(picked_color_rgb, cv2.COLOR_RGB2Lab)[0][0]
    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2Lab)
    delta_es = np.apply_along_axis(lambda lab_color: deltaE_cie76(picked_color_lab, lab_color), 2, lab_image)
    mask = delta_es < threshold
    result_image = image.copy()
    result_image[mask] = [0, 255, 0] 
    return result_image

def main(image_path):
    color_picker(image_path)
    image = cv2.imread(image_path)
    similar_colors_image = highlight_similar_colors(image, picked_color)
    plt.imshow(similar_colors_image)
    plt.title("Similar Colors Highlighted")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing images.')
    parser.add_argument('-i', '--image', type=str, default='image_0.jpeg', help='Image path')

    # Parsing parameters.
    args = parser.parse_args()
    image_path = f"input_images/{args.image}"
    main(image_path)