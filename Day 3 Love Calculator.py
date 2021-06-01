# -*- coding: utf-8 -*-
"""
Created on Sat May 29 04:22:02 2021

@author: Septhiono
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
name3=name1+name2
true=name3.count('t')+name3.count('r')+name3.count('u')+name3.count('e')
love=name3.count('l')+name3.count('o')+name3.count('v')+name3.count('e')
score=int(str(true)+str(love))
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

