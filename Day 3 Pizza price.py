# -*- coding: utf-8 -*-
"""
Created on Sat May 29 03:44:02 2021

@author: Septhiono
"""
# could use only 1 variable and add to it instead of 3 variables'
print("Welcome to Python Pizza Deliveries!")
sizes = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total=0
if sizes=='S':
    total+=15
elif sizes=='M':
    total+=20
elif sizes=='L':
    total+=25

if add_pepperoni=='Y':
    if sizes=='S':
        total+=2
    else:
        total+=3
elif add_pepperoni=='N':
    total+=0    

if extra_cheese =="Y":
    total+=1
elif extra_cheese=='n':
    total+=0

print("Your final bill is :$",total)