# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:39:16 2023

@author: 97154
"""
#In the first call, we use positional arguments to specify the size and message. In the second call, we use keyword arguments to specify the size and message. Both calls will print a sentence summarizing the shirt size and message.
"""
"""
def make_shirt(size, message):
    print(f"Creating a {size} shirt with the message: '{message}'")

# Call the function using positional arguments
make_shirt("medium", "Hello, World!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python Lover")
