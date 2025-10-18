# Project 1: Number Guessing Game 🔢
# Requirements:

# The program must generate a random integer between 1 and 50.

# The user should be prompted to enter their guess.

# After each guess, the program will tell the user if their guess is "Too high" or "Too low".

# If the user guesses the correct number, the program should print a success message like "Correct! You guessed it!" and then the game ends.

# Bonus: Keep track of the number of attempts it takes the user to guess the number and display it at the end.
import random
# if prog_choice-human_choice=>5:
#     print("Too high")
counter=0
while True:
    prog_choice=random.randint(1, 50)
    human_choice=int(input("Choose a number: "))
    print("\tThe comps Number: ",prog_choice)
    if prog_choice==human_choice:
        print("Correct! You guessed it!")
        break
    counter+=1
print("Number of times it took for you to guess: ",counter)