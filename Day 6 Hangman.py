# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:56:36 2021

@author: Septhiono
"""
import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)


def program():
    chosen_word= random.choice(word_list)

    print("You have 6 lives.")
    display=list()
    display=["_"]*len(chosen_word)
    life=6
    wrong=''
    while life>0:
        guess=input("please guess a letter: ").lower()
        count=0
        
        if guess in chosen_word:
            print(f"Letter {guess} is in the word, {stages[life]} ")
            if guess in display:
                print("You have already guessed ", guess)

            for i in chosen_word:        
                if i==guess:
                    display[count]=i          
                count+=1        
        elif guess not in chosen_word:
            
            if guess in wrong:
                print("You have tried this letter,it is not in the word")
                
            else:
                life-=1
                print(wrong)
                if wrong=='':
                    wrong=guess
                else:    
                    wrong=wrong+guess
                print(f"Letter {guess} is not in the word, {stages[life]} \n You have {life} lives remaining")
                print(guess)
                print("a",wrong)
                
            
        
        print(display)
        
        a= ''.join(display)
        if a==chosen_word:
            print("Congrats you won, the word is ",chosen_word)
            break
        elif life==0:
            print("You lost, the word is ", chosen_word)
while True:
     program()
     again=input("Do you wanna play again?").lower()
     if again == 'yes' or again=='y':
         continue
     else:
         print("Thank you for playing, Goodbye")
         break
