# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:42:11 2023

@author: 97154
"""
#The default values for size and message are set to "large" and "I love Python," respectively. 
#You can create shirts without specifying size or message parameters, and they will default to "large" and "I love Python." 
#Additionally, you can create shirts with custom sizes and messages by providing the desired values as arguments.
"""
"""
def make_shirt(size="large", message="I love Python"):
    print(f"Creating a {size} shirt with the message: '{message}'")

# Create a large shirt with the default message
make_shirt()

# Create a medium shirt with the default message
make_shirt(size="medium")

# Create a small shirt with a custom message
make_shirt(size="small", message="Python Programmer")
