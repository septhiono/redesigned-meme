import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand=[rock,paper,scissor]
while True:
    try:
        player=int(input("Please choose your hand, 0=rock, 1=paper, 2=scissor\n"))
    except:
        print("Please input number only")
        continue

    if player>2 or player<0:
        print("Wrong Number, Please try again")
        continue    
    computer=random.randint(0,2)
    a=hand[(player)]
    b=hand[computer]
    print(f"Player chose {a}, Computer chose {b}")
    if player>computer:
        print('Player wins')
        if player==2 and computer==0:
            print("Computer wins")
    if computer>player:
        if player==0 and computer==2:
            print("Player wins")
        else:
            print('Computer wins')
    if player==computer:
        print("Draw")
    if player>2:
        print("Wrong Number")
    asd=input("Do you want to try again?\n").lower()
    print(asd)
    if asd== 'yes':
        continue
    else:
        print("Thank you for playing")
        break
