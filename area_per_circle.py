#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 21, 2022
# This program calculates and displays the area and circumference of a circle
# with a diameter of 13cm.

import math


def main():
    # Initialize Variables
    diameter = 13
    radius = diameter / 2
    # Calculates Area and Circumference
    area = round(math.pi * radius**2, 2)
    circumference = round(math.pi * diameter, 2)
    # Outputs the Area and Circumference to the user
    print("For a circle with a diameter of 13cm:")
    print(f"Area: {area}cm^2")
    print(f"Circumference: {circumference}cm")


if __name__ == "__main__":
    main()
