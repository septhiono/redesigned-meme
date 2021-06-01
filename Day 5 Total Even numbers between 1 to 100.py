# -*- coding: utf-8 -*-
"""
Created on Sat May 29 23:30:11 2021

@author: Septhiono
"""
even_total=0
for i in range (1,101):
    if i%2==0:
        even_total+=i
print(even_total)
even_total=0
for i in range(2,101,2): # start at 2 so every step will be even number
    even_total+=i
print(even_total)        