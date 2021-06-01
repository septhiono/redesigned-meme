# -*- coding: utf-8 -*-
"""
Created on Sat May 29 03:30:25 2021

@author: Septhiono
"""

year=int(input("Which year would you like to check?"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")