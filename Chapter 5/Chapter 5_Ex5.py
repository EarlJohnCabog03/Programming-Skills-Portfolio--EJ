# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:14:05 2023

@author: 97154
"""
Question Chapter 5 Exercise 5.
#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about
#each pet

   
Explanation:
#I create a list called pets containing dictionaries, where each dictionary represents a different pet with keys "kind" for the kind of animal and "owner" for the owner's name.
#The loop iterates through the list of pets and prints information about each pet using f-strings, including the kind of animal and the owner's name. Each pet's information is separated by a newline for better readability.
"""
#Code:
"""

# Create a list of dictionaries representing different pets
pets = [
    {"kind": "Dog", "owner": "Alice"},
    {"kind": "Cat", "owner": "Bob"},
    {"kind": "Parrot", "owner": "Charlie"},
    {"kind": "Fish", "owner": "David"},
    {"kind": "Rabbit", "owner": "Eve"}
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}\n")
