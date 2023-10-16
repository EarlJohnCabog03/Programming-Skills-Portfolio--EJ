# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:26:31 2023

@author: 97154
"""
"""
Exercise 7 seeing the world
"""
Question Chapter 3 Exercise 7.
#Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse() to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

Explanation:
#The list of places to visit using methods like sorted(), reverse(), 
#and sort(). It also shows that the original list remains unaffected when these methods are used.
   
"""
#Code:
"""
# List of places to visit
places_to_visit = ["Paris", "Tokyo", "Venice", "New York", "Machu Picchu"]

# Print the list in its original order
print("Original Order:", places_to_visit)

# Print the list in alphabetical order without modifying the original list
print("Alphabetical Order:", sorted(places_to_visit))

# Show that the original list is still in its original order
print("Original Order (still):", places_to_visit)

# Print the list in reverse alphabetical order without modifying the original list
print("Reverse Alphabetical Order:", sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("Original Order (still):", places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("Reversed Order:", places_to_visit)

# Change the order of the list again using reverse()
places_to_visit.reverse()
print("Back to Original Order:", places_to_visit)

# Change the order of the list using sort()
places_to_visit.sort()
print("Alphabetical Order (changed):", places_to_visit)

# Change the order of the list using sort() for reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Reverse Alphabetical Order (changed):", places_to_visit)
"""
"""



