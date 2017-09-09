# Basic guessing game I wrote for practice whilst learning python

low,hi = 1,1024
guesses = 0

import random as r

the_num = r.randint(low,hi)
print("I'm thinking of a number between",low,"and",hi)

for i in range(low,hi):
    guess = int(input("What is your guess: "))
    guesses += 1
    if guess > the_num:
        print("\nLower!\n")
    elif guess < the_num:
        print("\nHigher!\n")
    else:
        break

if guesses >= 12:
    print("\nThat took",guesses,"guesses, you suck arse!\n")
elif guesses <= 4:
    print("\nThat took",guesses,"guesses, you're fucking amazing!\n")
else:
    print("\nThat took",guesses,"guesses... You're the luke warm water of people.\n")
