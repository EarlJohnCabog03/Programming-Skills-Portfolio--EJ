# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:49:18 2023

@author: 97154
"""
Question Chapter 4 Exercise 2
#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#•Write one version of this program that runs the if block and another that runs the else block.

Code:
#Version 1 (Runs the if block - Alien is green):
#In this version, the alien_color is set to 'green', and the if statement checks if it's green. Since it is green, 
#the if block is executed, and the message "Player just earned 5 points for shooting the alien" is printed.
"""
"""
alien_color = 'green'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")
    
#Version 2 (Runs the else block - Alien is not green):
#In this version, the alien_color is set to 'red' (or any color other than 'green'). The if statement checks if it's green,
#but it's not. Therefore, the else block is executed, and the message "Player just earned 10 points" is printed.
alien_color = 'red'  # You can set this to any color other than 'green'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")
"""
"""



