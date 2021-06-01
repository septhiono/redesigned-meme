# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:39:08 2021

@author: Septhiono
"""

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
column=int(position[0])
row=int(position[1])
x=map[row-1]
x[column-1]='x'

print(x)






print(f"{row1}\n{row2}\n{row3}")