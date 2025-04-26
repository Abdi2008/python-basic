import random


username=input("Enter your choice between ; rock,paper,scissor: ").lower()
computer=random.choice(["rock","paper","scissor"])
if username == computer:
     print("DRAW")
elif username == "rock" and computer == "paper":
     print("Computer Won")
elif username == "rock" and computer == "scissor":
     print("You Won")
elif username == "scissor" and computer == "rock":
     print("Computer Won")
elif username == "scissor" and computer == "paper":
     print("You Won")
elif username == "paper" and computer == "rock":
     print("You Won")
elif username == "paper" and computer == "scissor":
     print("Computer Won")
print("Your Computer choice ",computer)