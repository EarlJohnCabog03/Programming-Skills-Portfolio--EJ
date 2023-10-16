# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:57:22 2023

@author: 97154
"""
Question Chapter 4 Exercise 4.
#Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#•If the person is less than 2 years old, print a message that the person is a baby.
#•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#•If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#•If the person is at least 13 years old but less than 20, print a message that the person is a teenager
#•If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#•If the person is age 65 or older, print a message that the person is an elder.



Explanation:
#We first get the person's age as input. Then,
#we use a series of if-elif-else statements to check the age against the given criteria and print the appropriate message based on the age category.
"""
#Code:
"""
age = int(input("Enter the person's age: ")

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
