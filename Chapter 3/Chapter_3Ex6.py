# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:35:29 2023

@author: 97154
"""
"""
Ex 6 Shriking Guest list
"""
Question Chapter 3 Exercise 6
#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.  

Explanation:
# print a message stating that only two people can be invited. Then, we use a while loop with pop() to remove guests one by one while there are more than two guests in the list, apologizing to each removed guest. 
#Afterward, we print a message to the two remaining guests, and finally, we use del to remove the last two names, making the list empty.


"""
#Code:
"""
# List of people to invite to dinner
guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci", "Isaac Newton"]

# Print a message stating that only two people can be invited
print("I can invite only two people for dinner.")

# Use pop() to remove guests one at a time until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message to the two people still on your list
for guest in guests:
    print(f"{guest}, you're still invited to dinner.")

# Use del to remove the last two names from your list
del guests[0]  # Remove the first person
del guests[0]  # Remove the second person

# Print the updated list to ensure it's empty
print("Updated list of guests:", guests)
"""
"""
