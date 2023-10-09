# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:25:14 2023

@author: 97154
"""
#We start with a list of sandwich orders called sandwich_orders and an empty list for finished sandwiches called finished_sandwiches.
#We use a while loop to process each sandwich order from the sandwich_orders list.
#Inside the loop, we check if the current sandwich is "pastrami" (case-insensitive). If it is, we print a message indicating that it's unavailable. Otherwise, we make the sandwich, print a message, and move it to the finished_sandwiches list.
#After all sandwiches have been processed, we print a message listing each finished sandwich.
"""
"""
# Create a list of sandwich orders
sandwich_orders = ["tuna", "turkey", "pastrami", "vegetarian", "ham"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    # Check if the sandwich is pastrami (assuming it needs to be removed)
    if current_sandwich.lower() == "pastrami":
        print(f"Sorry, we're out of {current_sandwich.capitalize()}!")
    else:
        print(f"I made your {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)

# Print a message listing each finished sandwich
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
