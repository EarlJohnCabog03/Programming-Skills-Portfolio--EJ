# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:11:15 2023

@author: 97154
"""
#We create a dictionary called rivers with three major rivers as keys and the countries they run through as values.
#The first loop iterates through the dictionary to print a sentence about each river using f-strings.
#The second loop prints the names of each river by iterating through the keys of the dictionary.
#The third loop prints the names of each country by iterating through the values of the dictionary.
"""
"""

# Create a dictionary of major rivers and the countries they run through
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the names of each river
print("\nList of rivers:")
for river in rivers.keys():
    print(river)

# Print the names of each country
print("\nList of countries:")
for country in rivers.values():
    print(country)
