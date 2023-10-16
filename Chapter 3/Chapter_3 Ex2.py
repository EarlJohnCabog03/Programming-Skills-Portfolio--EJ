# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:30:54 2023

@author: 97154
"""
"""
Ex 2 Greetings
"""
Question Chapter 3 Exercise 2.
#Start with the list you used in Exercise 1, but instead of just
#printing each person’s name, print a message to them. The text of each message should be the same, but each message should be
#personalized with the person’s name.

Explanation :
#Use a for loop to iterate through the names list and create a
#personalized message for each person by including their name in the message. Each message is printed with the respective person's name.
"""
#Code:
"""
# Define a list of your friends' names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Print a personalized message to each person
for name in names:
    message = f"Hello, {name}! I hope you're having a great day."
    print(message)
"""
"""
