from sklearn.cluster import KMeans
from PIL import Image
from skimage.color import rgb2lab, lab2rgb
import numpy as np
import argparse

def kmeans_quantize(image, num_colors):
   img_array = np.array(image)
   lab_array = rgb2lab(img_array.reshape((-1, 3)))
   kmeans_model = KMeans(n_clusters=num_colors)
   clustered_labels = kmeans_model.fit_predict(lab_array)
   quantized_lab_array = kmeans_model.cluster_centers_[clustered_labels]
   quantized_rgb_array = lab2rgb(quantized_lab_array.reshape(img_array.shape))
   return Image.fromarray((quantized_rgb_array * 255).astype(np.uint8))

def uniform_quantize(img, n_bins):
    np_img = np.array(img)
    max_val = 255
    bin_width = max_val // n_bins
    quantized_img = ((np_img // bin_width) * bin_width + bin_width // 2)
    return Image.fromarray(np.uint8(quantized_img))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing images.')
    parser.add_argument('-i', '--image', type=str, default='input_images/image_0.jpeg', help='Image path')

    # Parsing parameters.
    args = parser.parse_args()
    image_path = f"input_images/{args.image}"

    image = Image.open(image_path)
    
    image_kmeans_quantized= kmeans_quantize(image,4)
    image_uniform_quantized = uniform_quantize(image,4)

    image.show()
    image_kmeans_quantized.show()
    image_uniform_quantized.show()