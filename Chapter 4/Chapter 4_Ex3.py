# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:51:51 2023

@author: 97154
"""
"""
Alien colors #3
"""
Question Chapter 4 Exercise 3
#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.


#Version 1 (Green Alien - Earns 5 points):
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")



#Version 2 (Yellow Alien - Earns 10 points):
alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")




#Version 3 (Red Alien - Earns 15 points):
alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")

