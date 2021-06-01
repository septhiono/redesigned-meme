import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display=["_"]*len(chosen_word)
print(display)
print(chosen_word)
guess = input("Guess a letter: ").lower()


print("weong")
