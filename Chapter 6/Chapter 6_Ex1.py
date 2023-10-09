# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:18:18 2023

@author: 97154
"""
#We use a while loop to repeatedly prompt the user for input.
#Inside the loop, we use the input function to get the user's input and store it in the topping variable.
#We check if the user entered 'quit' as the topping. If they did, we break out of the loop to end the program.
#Otherwise, we print a message indicating that the entered topping will be added to their pizza.
#This loop will continue until the user enters 'quit', and it will add each entered topping to their pizza.
"""
"""

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping == 'quit':
        break
    
    print(f"I'll add {topping} to your pizza.")