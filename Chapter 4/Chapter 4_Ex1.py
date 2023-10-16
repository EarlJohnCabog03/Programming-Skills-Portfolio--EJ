# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:46:41 2023

@author: 97154
"""
Question Chapter 4 Exercise 1.
#Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""
"""

#Code:
#Passing Version (Alien is green)
#In this version, the alien_color is set to 'green', and the if statement checks if it's green. Since it is, the message "Player just earned 5 points" is printed.
alien_color = 'green'

if alien_color == 'green':
    print("Player just earned 5 points.")


    
#In this version, the alien_color is set to 'red' (or 'yellow'). The if statement checks if it's green, but it's not. Therefore, there will be no output because the condition is not met.
#Failing Version (Alien is not green):
alien_color = 'red'  # You can set this to 'yellow' or 'red'

if alien_color == 'green':
    print("Player just earned 5 points.")

