# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:06:13 2023

@author: 97154
"""
Question Chapter 5 Exercise 2.
#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
#their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between
#each word-meaning pair in your output.  


Explanation:
#In this example, we've created a dictionary called glossary with programming terms as keys and their corresponding meanings as values. 
#We then use a for loop to iterate through the dictionary and print each word and its meaning, with a newline character (\n) inserted between each word-meaning pair for better formatting.
"""
#code:
"""
    
# Create a glossary dictionary with programming terms and meanings
glossary = {
    "variable": "A container for storing data in a program.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "A control structure that repeats a block of code until a condition is met.",
    "boolean": "A data type that represents true or false values.",
    "algorithm": "A step-by-step set of instructions for solving a specific problem."
}

# Print each word and its meaning with a newline in between
for word, meaning in glossary.items():
    print(word + ":")
    print(meaning + "\n")
"""
"""
