# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:14:08 2021

@author: ACER
"""
import matplotlib.pyplot as plt
from PIL import Image


def render_img(img):
    """
    Opens and displays an image using matplotlib.

    Parameters:
        img (str): The file path of the image to be displayed.

    Returns:
        PIL.Image.Image: The opened image object.

    Raises:
        FileNotFoundError: If the image file is not found in the provided path.
        OSError: If the file cannot be opened or is not recognized as a valid image format.
        Exception: Any other unhandled exception that might occur during image processing.

    Displays the image using matplotlib's `imshow` and `show` functions. It opens the image
    specified by the `img` parameter, which should be a valid file path of an image.

    The function returns the opened image object from the PIL library (Pillow).

    Example:
        image_path = "path/to/image.jpg"
        img = render_img(image_path)

    Note:
        Make sure you have the necessary libraries installed:
        - PIL (Pillow) for image processing: `pip install Pillow`
        - matplotlib for displaying the image: `pip install matplotlib`
    """

    image = Image.open(img)
    plt.imshow(image)
    plt.show()
    return image


def auto_resize(img_1, img_2):
    """
    Resize the second image to match the size of the first image and return the master size.

    Parameters:
        img_1 (PIL.Image.Image): The first image (reference image) to determine the size.
        img_2 (PIL.Image.Image): The second image to be resized.

    Returns:
        tuple: A tuple containing the width and height of the master size determined
               by the first image.

    Resizes the second image (img_2) to match the dimensions (width and height) of the first
    image (img_1). The function uses the PIL library's `resize` method to perform the resizing.

    Note:
        - Both img_1 and img_2 should be valid PIL image objects.
        - The function does not modify the original images but returns the resized version of img_2.

    Example:
        from PIL import Image

        # Assuming img1 and img2 are valid PIL image objects
        img1 = Image.open("path_to_img1.jpg")
        img2 = Image.open("path_to_img2.jpg")

        master_size = auto_resize(img1, img2)
        # master_size will be a tuple containing the width and height of img1
        # img2 will be resized to match the dimensions of img1

    Raises:
        TypeError: If img_1 or img_2 is not a valid PIL image object.
        ValueError: If the images have invalid or mismatched dimensions.
        Exception: Any other unhandled exception that might occur during image processing.
    """

    master_size = img_1.size
    img_2.resize((master_size[0], master_size[1]))
    return master_size


def img_merge(img_1, img_2, master_size):
    """
    Merge two images side by side and save the result.

    Parameters:
        img_1 (PIL.Image.Image): The first image to be placed on the left side.
        img_2 (PIL.Image.Image): The second image to be placed on the right side.
        master_size (tuple): A tuple containing the width and height of the master size.
                             Both images will be resized to match this master size.

    Returns:
        None

    Merges the two input images (img_1 and img_2) side by side and saves the resulting
    merged image. The images will be resized to match the dimensions specified in the
    master_size tuple.

    The merged image will be saved with the filename "merged.jpg" in the current working directory.

    Note:
        - img_1 and img_2 should be valid PIL image objects.
        - master_size should be a tuple with two elements representing the width and height
          (e.g., master_size = (width, height)).
        - The function modifies the input images by resizing them to match the master size.
          To avoid modifying the original images, make a copy before passing them to the function.

    Example:
        from PIL import Image

        # Assuming img1 and img2 are valid PIL image objects
        img1 = Image.open("path_to_img1.jpg")
        img2 = Image.open("path_to_img2.jpg")

        master_size = (800, 600)
        img_merge(img1, img2, master_size)
        # The merged image will be saved as "merged.jpg" in the current working directory.

    Raises:
        TypeError: If img_1 or img_2 is not a valid PIL image object.
        ValueError: If the master_size is not a tuple or does not have two elements.
        Exception: Any other unhandled exception that might occur during image processing.
    """
    merged_image = Image.new(
        "RGB", (master_size[0] * 2, master_size[1]), (250, 250, 250)
    )
    merged_image.paste(img_1)
    merged_image.paste(img_2, (master_size[0], 0))
    output_path = "merged.jpg"
    merged_image.save(output_path)
    render_img(output_path)


if __name__ == "__main__":
    print("Running image_merger.py as main script...")
    print("Displaying image 1.jpg...")
    img_1 = render_img("1.jpg")
    print("Displaying image 2.jpg...")
    img_2 = render_img("2.jpg")
    print("Merging images 1.jpg and 2.jpg...")
    print("Merged image saved as merged.jpg")
    (img_merge(img_1, img_2, auto_resize(img_1, img_2)))
