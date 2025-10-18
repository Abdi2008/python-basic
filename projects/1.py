# Project 1: Number Guessing Game 🔢
# Requirements:

# The program must generate a random integer between 1 and 50.

# The user should be prompted to enter their guess.

# After each guess, the program will tell the user if their guess is "Too high" or "Too low".

# If the user guesses the correct number, the program should print a success message like "Correct! You guessed it!" and then the game ends.

# Bonus: Keep track of the number of attempts it takes the user to guess the number and display it at the end.
# import random
# # if prog_choice-human_choice=>5:
# #     print("Too high")
# counter=0
# while True:
#     prog_choice=random.randint(1, 50)
#     human_choice=int(input("Choose a number: "))
#     print("\tThe comps Number: ",prog_choice)
#     if prog_choice==human_choice:
#         print("Correct! You guessed it!")
#         break
#     counter+=1
# print("Number of times it took for you to guess: ",counter)
#THE CORRECTED VERSION
# Import the random module
import random

# --- FIX 1: Generate the number ONCE, before the loop starts ---
prog_choice = random.randint(1, 50) 
counter = 0

print("I've picked a number between 1 and 50. Can you guess it?")

while True:
    # Get the user's guess
    human_choice = int(input("Choose a number: "))
    
    # --- FIX 4: Increment the counter for every attempt ---
    counter += 1
    
    # --- FIX 3: Removed the line that revealed the answer ---

    # Check the guess
    if human_choice == prog_choice:
        print(f"Correct! You guessed it in {counter} tries!")
        break # Exit the loop on a correct guess
    # --- FIX 2: Added the "Too high" / "Too low" hints ---
    elif human_choice > prog_choice:
        print("Too high, try again!")
    else: # This covers if human_choice is less than prog_choice
        print("Too low, try again!")