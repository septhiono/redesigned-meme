# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:26:08 2021

@author: Septhiono
"""

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
score=0
count=0
for i in student_scores:
    score+=i
    count+=1
x=score/count
print(f"Total is {score}, average is {round(x)}")    