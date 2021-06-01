# -*- coding: utf-8 -*-
"""
Created on Sat May 29 23:03:08 2021

@author: Septhiono
"""

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


maxi=0
mini=student_scores[0]
for i in student_scores:
    if i>maxi:
        maxi=i
print(f"The Highest Score is {maxi}")

for i in student_scores:
    if i<mini:
        mini=i
print(f"The Lowest Score is {mini}")
