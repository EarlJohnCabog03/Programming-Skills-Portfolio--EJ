# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:21:45 2023

@author: 97154
"""
"""
"""
Question Chapter 6 Exercise 2.
#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their
#age, and then tell them the cost of their movie ticket

   
Explanation:
#We use a while loop to repeatedly prompt the user for their age.
#Inside the loop, we use the input function to get the user's age as input.
#We check if the user entered 'quit' (case-insensitive) to exit the loop. If they did, the loop ends.
#We convert the age input to an integer using int() so that we can compare it with numeric values.
#Based on the age entered, we use if-elif-else statements to determine and print the cost of the movie ticket.
#The loop continues until the user enters 'quit'.
"""
"""
while True:
    age = input("Please enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)  # Convert the input to an integer

    if age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
