
#Number guessing game

import random

def guess():
    num2 = random.randint(1,10)
    num = 0
    while num2 != num:
        num = int(input("Guess a number between 1 and 10\n"))
        print(f"Your number is {num}")

        if num == num2:
            print("You guessed a right number")
        elif num < num2:
            print(f"Number is bigger than {num}")
        else:
            print(f"number is less than {num}")

def comp_guess():
    num = 0
    feedback = ''
    low = 1
    high = 1000
    while feedback != 'c':
        if high != low:
            num = random.randint(low,high)
        else:
            num = low
        feedback = input(f"Is {num} the number you guessed? high (h), low (l), correct(c)")

        if feedback == 'h':
            low = num+1
        elif feedback == 'l':
            high = num-1
    
    print(f"Yayy! The number is {num}")


comp_guess()
guess()