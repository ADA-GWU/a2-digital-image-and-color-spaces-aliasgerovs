# Digital Images and Color Spaces

This repo provides a set of utilities for various image processing tasks, including color picking, color quantization, grayscale conversion, and color adjustment.

## Overview

The repo consists of several Python scripts, each performing a specific image processing task:

1. **Color Picking:** Allows users to select a color from an image by clicking on it.
2. **Highlighting Similar Colors:** Highlights colors similar to the picked color in an image.
3. **Color Quantization:** Quantizes the colors in an image using K-means clustering or uniform quantization.
4. **Grayscale Conversion:** Converts an image to grayscale using different methods.
5. **Color Adjustment:** Adjusts hue, saturation, brightness, and lightness of an image.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/ADA-GWU/a2-digital-image-and-color-spaces-aliasgerovs.git
cd a2-digital-image-and-color-spaces-aliasgerovs
```


## Install the required Python packages:

``` 
pip install -r requirements.txt

```

## Input Images:

- image_0.jpeg
- image_1.jpeg
- image_2.jpeg
- image_3.jpeg
- image_4.jpeg
- image_5.jpeg
- image_6.jpeg
- image_7.jpeg

## Grayscale Conversion

#### Parameteres:

`-i`: Input Image Name

```

python grayscale_conversion.py -i path/to/the/image.jpg


```

### Example:

<img width="654" alt="image" src="https://github.com/ADA-GWU/a2-digital-image-and-color-spaces-aliasgerovs/assets/49990436/79ae3e6c-b455-463d-a443-a703a6d0ed75">


## Color Quantization

#### Parameteres:

`-i`: Input Image Name

```
python color_quantization.py -i path/to/the/image.jpg

```

### Example:

<img width="486" alt="image" src="https://github.com/ADA-GWU/a2-digital-image-and-color-spaces-aliasgerovs/assets/49990436/a2383e6a-eb8c-4372-a339-6b2b39ddac30">



## Color Adjustment

####   -i, --image: Path to the input image file (required)
####  -ha, --hue_adjustment: Hue adjustment value (default: 0.1)
####   -sa, --saturation_adjustment: Saturation adjustment value (default: 0.1)
####   -ba, --brightness_adjustment: Brightness adjustment value (default: 0.1)
####   -lf, --lightness_factor: Lightness factor value (default: 10)


```
python color_adjustment.py -i path/to/the/image.jpg -ha 0.1 -sa 0.1 -ba 0.1 -lf 10

```

### Example:

<img width="486" alt="image" src="https://github.com/ADA-GWU/a2-digital-image-and-color-spaces-aliasgerovs/assets/49990436/6b1a4a49-fc65-42dd-98d3-2bf6d7548c15">


## Highlighting Similar Colors

#### Parameteres:

`-i`: Input Image Name

```

python similar_colors.py -i path/to/the/image.jpg

```

### Example:

<img width="486" alt="image" src="https://github.com/ADA-GWU/a2-digital-image-and-color-spaces-aliasgerovs/assets/49990436/41e40e0b-78af-489a-8279-1f72a0606e45">



