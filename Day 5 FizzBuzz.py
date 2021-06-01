# -*- coding: utf-8 -*-
"""
Created on Sun May 30 00:13:57 2021

@author: Septhiono
"""
count=0
for i in range (1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz",i)
        
    elif i%3==0:
        print("Fizz",i)
        
    elif i%5==0:
        print("Buzz",i)
        
    else:
        print(i)
        