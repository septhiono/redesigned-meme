print('Welcome to the tip calculator')
bill = float(input('What was the total bill? $'))

tip= float(input('What percentage tip would you like to give? '))
people = float(input("How many people split the bill? "))

pay= bill*(1+tip/100)/people
pay=float(pay)
print("Each person should pay: $",round(pay,2))
