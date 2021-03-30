import time
import random
import sys

print("Welcome To Mastermind!")
print("How To Play:")
time.sleep(1)
print("1. The Computer will select 4 numbers from 1 to 10, you must guess all 4 numbers in the right order.")
time.sleep(1)
print("2. Each time you guess, the computer will tell you how much numbers did you guess right, and tell you if those "
      "numbers were in the correct order.")
time.sleep(1)
print("3.There is no limit to how much guesses you can use.")
time.sleep(1)
print("You win by guessing all the correct numbers in the right order")
startgame = input("Ready to begin? (Enter anything to continue)")
while True:
    try:
        level = int(input("select ur level: "))
    except ValueError:
        print("Enter A NUMBER.")
        continue
    else:
        print("Ok! Level", level, "it is!")
        break

q1 = random.randint(1, level)
q2 = random.randint(1, level)
q3 = random.randint(1, level)
q4 = random.randint(1, level)
num = [q1, q2, q3, q4]
tries = 0
guess = 0
while num != guess:
    a1 = int(input("Guess the first number: "))
    a2 = int(input("Guess the second number: "))
    a3 = int(input("Guess the third number: "))
    a4 = int(input("Guess the fourth number: "))
    guess = [a1, a2, a3, a4]

    tries += 1
    if a1 > q1:
        print("The First number is too BIG")
    if a1 < q1:
        print("The First number is too SMALL")
    if a2 > q2:
        print("The Second number is too BIG")
    if a2 < q2:
        print("The Second number is too SMALL")
    if a3 > q3:
        print("The Third number is too BIG")
    if a3 < q3:
        print("The Third number is too SMALL")
    if a4 > q4:
        print("The Fourth number is too BIG")
        continue
    if a4 < q4:
        print("The Fourth number is too SMALL")
        continue
    if guess == num:
        print('Well Done!')
        print("It took you", tries, "to guess all four numbers!")
        restart = input("Do you want to try again? (y/n)")
        if restart == "y":
            exec(open('main.py').read())
        else:
            sys.exit()
