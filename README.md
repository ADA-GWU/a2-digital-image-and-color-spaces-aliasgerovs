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

## Highlighting Similar Colors

```

python similar_colors.py -i path/to/your/image.jpg

```

## Color Quantization


```
python color_quantization.py -i path/to/your/image.jpg

```

## Grayscale Conversion

```

python grayscale_conversion.py -i path/to/your/image.jpg


```

## Color Adjustment

```
python color_adjustment.py -i path/to/your/image.jpg -ha 0.1 -sa 0.1 -ba 0.1 -lf 10

```
