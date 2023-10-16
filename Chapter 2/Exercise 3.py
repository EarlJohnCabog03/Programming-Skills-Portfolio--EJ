# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:28:11 2023

@author: 97154
"""
Question:
#Tidy up the code to make it easier to understand
#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().


"""
"""

Explanation.
#This code uses the \t and \n characters for whitespace and demonstrates the effects of the lstrip(), rstrip(), and strip() 
#functions to remove the leading, trailing, and both leading and trailing whitespace, respectively.
"""
"""
#Code:
# Define a person's name with whitespace
name = "\t \n   John Doe   \t \n"

# Print the name with whitespace
print("Name with Whitespace:")
print(name)

# Print the name after left stripping
print("Left Stripped Name:")
print(name.lstrip())

# Print the name after right stripping
print("Right Stripped Name:")
print(name.rstrip())

# Print the name after stripping from both sides
print("Stripped Name:")
print(name.strip())

"""
"""
