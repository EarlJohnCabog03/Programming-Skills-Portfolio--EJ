# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:47:04 2023

@author: 97154
"""
Question Chapter 1 Exercise 5.
#Write a Python program which accepts the radius of a circle from the user and compute the area.

Explanation:
#we first import the math module to access the constant pi. 
#Then, we prompt the user to enter the radius, convert it to a float, calculate the area, and print the result with two decimal places.
"""
#Code:
"""

import math

# Accept the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius**2)

# Print the result
print(f"The area of the circle with radius {radius} is {area:.2f}")

"""
"""
