from PIL import Image
import numpy as np
import matplotlib
import colorsys
import argparse

def change_hue(img, hue_adjustment):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img_array = np.array(img)
    hsv_image = matplotlib.colors.rgb_to_hsv(img_array / 255.0)
    hsv_image[:, :, 0] += hue_adjustment
    hsv_image[:, :, 0] = np.mod(hsv_image[:, :, 0], 1)
    rgb_image = matplotlib.colors.hsv_to_rgb(hsv_image)
    return Image.fromarray((rgb_image * 255).astype(np.uint8))

def change_saturation(img, saturation_adjustment):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img_array = np.array(img)
    hsv_image = matplotlib.colors.rgb_to_hsv(img_array / 255.0)
    hsv_image[:, :, 1] += saturation_adjustment
    hsv_image[:, :, 1] = np.mod(hsv_image[:, :, 1], 1)
    rgb_image = matplotlib.colors.hsv_to_rgb(hsv_image)
    return Image.fromarray((rgb_image * 255).astype(np.uint8))

def change_brightness(img, brightness_adjustment):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img_array = np.array(img)
    hsv_image = matplotlib.colors.rgb_to_hsv(img_array / 255.0)
    hsv_image[:, :, 2] += brightness_adjustment
    hsv_image[:, :, 2] = np.mod(hsv_image[:, :, 2], 1)
    rgb_image = matplotlib.colors.hsv_to_rgb(hsv_image)
    return Image.fromarray((rgb_image * 255).astype(np.uint8))

def change_lightness(img, lightness_factor):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    data = img.getdata()
    new_data = []
    for item in data:
        h, s, l = colorsys.rgb_to_hls(item[0]/255.0, item[1]/255.0, item[2]/255.0)
        l = max(0, min(1, l * lightness_factor))
        new_color = colorsys.hls_to_rgb(h, l, s)
        new_color = tuple([int(x * 255) for x in new_color])
        new_data.append(new_color)
    img.putdata(new_data)
    return img

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing images.')
    parser.add_argument('-i', '--image', type=str, default='image_0.jpeg', help='Image path')
    parser.add_argument('-ha', '--hue_adjustment', type=float, default=0.1, help='hue_adjustment')
    parser.add_argument('-sa', '--saturation_adjustment', type=float, default=0.1, help='saturation_adjustment')
    parser.add_argument('-ba', '--brightness_adjustment', type=float, default=0.1, help='brightness_adjustment')
    parser.add_argument('-lf', '--lightness_factor', type=float, default=10, help='lightness_factor')

    # Parsing parameters.
    args = parser.parse_args()
    image_path = f"input_images/{args.image}"
    hue_adjustment = args.hue_adjustment
    saturation_adjustment = args.saturation_adjustment
    brightness_adjustment = args.brightness_adjustment
    lightness_factor = args.lightness_factor

    image = Image.open(image_path)
    
    hue_changed_image = change_hue(image, hue_adjustment)
    sat_changed_image = change_saturation(image, saturation_adjustment)
    bright_changed_image = change_brightness(image, brightness_adjustment)
    light_changed_image = change_lightness(image, lightness_factor)

    hue_changed_image.show()
    sat_changed_image.show()
    bright_changed_image.show()
    light_changed_image.show()