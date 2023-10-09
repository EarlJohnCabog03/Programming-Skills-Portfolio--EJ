# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:06:06 2023
3
@author: 97154
"""
"""
exercise 3 print date and time
"""""
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))