#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 21, 2022
# This program calculates and displays the area and circumference of a circle
# with a radius of 15mm.

import math


def main():
    # Initialize Variables
    radius = 15
    diameter = radius * 2
    # Calculates Area and Circumference
    area = math.pi * radius**2
    circumference = math.pi * diameter
    # Outputs the Area and Circumference to the user
    print("For a circle with a radius of 15mm:")
    print(f"Area: {area}mm^2")
    print(f"Circumference: {circumference}mm")


if __name__ == "__main__":
    main()
