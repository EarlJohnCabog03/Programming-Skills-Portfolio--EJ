# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:06:06 2023
3
@author: 97154
"""
"""
Exercise 3 print date and time
"""
Question Chapter 1 Exercise 3.
#Write a Python program to display the current date and time.


Explanation
#The datetime module, retrieves the current date and time using datetime.datetime.now(), and then prints the result, showing the current date and time.
"""
#Code:
"""
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
"""
"""
