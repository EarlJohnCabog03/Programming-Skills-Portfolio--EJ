# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:57:22 2023

@author: 97154
"""

age = 30  # You can change the age to test different scenarios

if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
