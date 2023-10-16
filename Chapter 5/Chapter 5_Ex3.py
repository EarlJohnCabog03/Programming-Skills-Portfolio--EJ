# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:08:58 2023

@author: 97154
"""
"""
"""
Question Chapter 5 Exercise 3.
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""
"""
Explanation:
#This code defines the original glossary and adds five more terms to it. 
#Then, it uses a for loop to iterate through the dictionary and print each term along with its definition. Adding or modifying terms will automatically include them in the output when you run the program.
"""
#code:
"""
# Define the glossary dictionary
glossary = {
    'variable': 'A container for storing data.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.',
    'function': 'A reusable block of code.',
    'loop': 'A structure for repeating a set of instructions.',
    'module': 'A file containing Python code.',
    'class': 'A blueprint for creating objects.',
    'method': 'A function associated with an object.',
    'tuple': 'An ordered, immutable collection of items.',
    'conditional statement': 'A decision-making structure.'
}

# Loop through the dictionary to print keys and values
for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")

# Output all the terms and their definitions



