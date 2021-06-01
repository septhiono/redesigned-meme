# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:05:22 2021

@author: Septhiono
"""

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position=int(position)
if position ==11:
    row1[0]='x'
elif position==12:
    row1[1]='x'
elif position==13:
    row1[2]='x'
elif position==21:
    row2[0]='x'
elif position==22:
    row2[1]='x'
elif position==23:
    row2[2]='x'
elif position==31:
    row3[0]='x'
elif position==32:
    row3[1]='x'
else:
    row3[2]='x'

print(position)

print(f"{row1}\n{row2}\n{row3}")