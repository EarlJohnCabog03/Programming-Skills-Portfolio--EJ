# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:44:16 2023

@author: 97154
"""
"""
"""
Question Chapter 7 Exercise 5.
#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,
#such as Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

Explantion:
#The describe_city() function with two parameters, city and country, with country having a default value of "Unknown."
#We call the function three times with different cities and countries, including one city (Tokyo) where we don't provide a custom country name, so it uses the default value.
"""
#Code:
"""
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("Tokyo")
