# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:06:06 2023
3
@author: 97154
"""
"""
Exercise 3 Write a Python program to display the current date and time.
"""
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
