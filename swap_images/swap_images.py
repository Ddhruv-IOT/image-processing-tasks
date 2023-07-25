# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 22:57:19 2021

@author: ACER
"""

import matplotlib.pyplot as plt
import cv2


def load_img(img):
    """
    Load an image from the specified file path using OpenCV (cv2) and convert it to RGB color space.

    Note: Ensure that you have installed OpenCV (`cv2`) before using this function.

    Parameters:
        img (str): The file path of the image to be loaded.

    Returns:
        numpy.ndarray: The image data represented as a NumPy array with RGB color channels.

    Example:
        img_path = 'path/to/your/image.jpg'
        loaded_image = load_img(img_path)
        # `loaded_image` will hold the image data in RGB format.
    """
    image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def render(img_obj):
    """
    Display an image using Matplotlib's `imshow` function.

    Parameters:
        img_obj: An image object to be displayed. The object should be compatible with `plt.imshow`.

    Returns:
        None

    Example:
        img = your_loaded_image_data_as_numpy_array  # Replace this with your actual image data
        render(img)
        # The image will be displayed in a separate window.
    """

    plt.imshow(img_obj)
    plt.show()


def swap(img_obj1, img_obj2):
    """
    Swap regions of two images and return the modified copies.

    This function performs a hardcoded region swap between two input images and returns the modified
    copies. The first image (img_obj1) has its top portion (100 rows from the top and 150 columns
    starting from column 50) replaced with the resized region from the second image (img_obj2). The
    second image (img_obj2) has its top-left portion (300 rows and 310 columns starting from column
    190) replaced with the resized region from the first image.

    Parameters:
        img_obj1: The first image object to perform the swap on.
        img_obj2: The second image object to perform the swap on.

    Returns:
        tuple: A tuple containing two modified image objects.

    Example:
        img1 = your_loaded_image_data_as_numpy_array1  # Replace this with your actual image data
        img2 = your_loaded_image_data_as_numpy_array2  # Replace this with your actual image data
        swapped_img1, swapped_img2 = swap(img1, img2)
        # `swapped_img1` will hold the first image with the specified region swapped,
        # and `swapped_img2` will hold the second image with the specified region swapped.
    """

    x, y = img_obj1, img_obj2
    y_cp = y.copy()
    x_cp = x.copy()

    x1 = x[:100, 50:200]
    face1_resize = cv2.resize(x1, (700, 299))  # dore
    y_cp[1:300, :700] = face1_resize
    y_cp = y_cp[:1000, :]

    y1 = y[:300, 190:500]
    face2_resize = cv2.resize(y1, (220, 100))  # man
    x_cp[1:101, :220] = face2_resize

    return x_cp, y_cp


if __name__ == "__main__":
    img_obj1 = load_img("d1.jpg")  # dore
    render(img_obj1)

    img_obj2 = load_img("10.jpg")  # man
    render(img_obj2)

    s1, s2 = swap(img_obj1, img_obj2)
    render(s1)
    render(s2)
