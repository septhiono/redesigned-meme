# -*- coding: utf-8 -*-
"""
Created on Sat May 29 02:35:30 2021

@author: Septhiono
"""

height=input("enter your height in m: ")
weight=input('enter your weight in kg: ')

bmi= float(weight)/float(height)**2
bmi=round(bmi,)
print("Your BMI is:",bmi)

if bmi<18.5:
    print("You are Underweight")
elif bmi<25:
    print("You Have a Normal Weight")
elif bmi<30:
    print("You are Slightly Overweight")
elif bmi<35:
    print("You are Obese")
else:
    (print("You are Clinically obese"))

    