# -*- coding: utf-8 -*-
"""
Created on Sat May 29 00:51:59 2021

@author: Septhiono
"""
name=input('What is your name?\n')
age=input('What is your current age?\n')
month=input('How many months since your birthday?\n')
days=input('How many extra days?\n')
year_left=90-int(age)
month=int(month)
days=int(days)
x=year_left*365-(month*30)-(days)
y=year_left*52-(month*4)-(days//7)
z=year_left*12-month-(days//30)

print(f"Hi {name}, if you live until 90 years old, You have {x} days, or {y} weeks, or {z} months left to live")
