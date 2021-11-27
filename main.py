
#Number guessing game

import random

num = int(input("Guess a number between 1 and 10\n"))
print(f"Your number is {num}")

num2 = random.randint(1,10)

if num == num2:
    print("You guessed a right number")
else:
    print("You guessed a wrong number")