#Number Guessing Game

import random

print("Hello!!! Welcome to the number guessing game. I'm going to pick a number between 1 to 100 for you.")
print("Picking a number...")

guess = int(input("What is your guess? : "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    guess_count += 1

    if guess < correct_number:
      guess = int(input(" Wrong!!! You need to guess a bit Higher... What is your guess? : "))

    else:
      guess = int(input(" Wrong!!! You need to guess a bit Lower... What is your guess? : "))

print(f'Congratulation!! The Right answer was {correct_number}. It took you {guess_count} gusses!')  
