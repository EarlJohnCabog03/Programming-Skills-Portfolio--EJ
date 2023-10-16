# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:46:41 2023

@author: 97154
"""
Question Chapter 4 Exercise 1.
#Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

#Code:
#Passing Version (Alien is green)
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

    
#In this version, the alien_color is 'green,' and the if statement tests if it's equal to 'green,' which is true. Therefore, the message is printed, and the player earns 5 points.
#Failing Version (Alien is not green):
alien_color = 'red'

if alien_color == 'green
