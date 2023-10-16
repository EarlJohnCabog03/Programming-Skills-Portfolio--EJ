# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:39:16 2023

@author: 97154
"""
"""
"""
Question Chapter 7 exercise 3
#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional
#arguments to make a shirt. Call the function a second time using keyword arguments.
"""
Explanation:
#In the first call, we use positional arguments to specify the size and message. In the second call, we use keyword arguments to specify the size and message. Both calls will print a sentence summarizing the shirt size and message.
"""
#code:
"""
"""
def make_shirt(size, message):
    print(f"Creating a {size} shirt with the message: '{message}'")

# Call the function using positional arguments
make_shirt("medium", "Hello, World!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python Lover")
