# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:24:12 2021

@author: ACER
"""
import numpy as np
import matplotlib.pyplot as plt
import time

def show(mg):
    time.sleep(1)
    plt.imshow(mg)
    plt.axis('off')
    plt.show()

def draw_landscape(width, height):
    # Create a blank canvas
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    print("Creating Blank canvas...")
    show(canvas)
   

    # Sky - a blue gradient
    sky_color = [135, 206, 235]
    for y in range(height):
        canvas[y, :, :] = sky_color
    print("Painting Sky...")
    show(canvas)
    

    # Ground - a green rectangle
    ground_color = [34, 139, 34]
    ground_height = height // 3
    canvas[-ground_height:, :, :] = ground_color
    print("Designing Ground...")
    show(canvas)

    # Sun - a yellow circle
    sun_color = [255, 255, 0]
    sun_center = (width // 4, height // 6)
    sun_radius = min(width, height) // 10
    for y in range(max(0, sun_center[1] - sun_radius), min(height, sun_center[1] + sun_radius)):
        for x in range(max(0, sun_center[0] - sun_radius), min(width, sun_center[0] + sun_radius)):
            if np.sqrt((x - sun_center[0])**2 + (y - sun_center[1])**2) < sun_radius:
                canvas[y, x, :] = sun_color
    print("Lighting up the Sun...")
    show(canvas)

    # Mountain - a brown triangle
    mountain_color = [139, 69, 19]
    mountain_height = height // 3
    mountain_base = width // 2
    for y in range(ground_height, ground_height + mountain_height):
        for x in range(mountain_base - (y - ground_height), mountain_base + (y - ground_height) + 1):
            canvas[y, x, :] = mountain_color
    print("Building Mountain...")
    show(canvas)
    time.sleep(2)
    return canvas

if __name__ == "__main__":
    width, height = 800, 600
    landscape = draw_landscape(width, height)
    print("The Landscape is ready! Enjoy!")
    plt.imshow(landscape)
    plt.axis('off')
    plt.show()
    print("Thank you for using our service!")
