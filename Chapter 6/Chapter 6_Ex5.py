# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:30:10 2023

@author: 97154
"""
#We've added more occurrences of 'pastrami' to the sandwich_orders list.
#We added a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
#As a result, no 'pastrami' sandwiches will end up in the finished_sandwiches list, and a message is printed to notify that the deli has run out of pastrami.
"""
"""
# Create a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ["tuna", "turkey", "pastrami", "vegetarian", "pastrami", "ham", "pastrami"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Notify the deli has run out of pastrami and remove all occurrences from sandwich_orders
print("Sorry, we've run out of pastrami!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each finished sandwich
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
