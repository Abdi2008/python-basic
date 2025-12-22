# def greet():
#     print("welcome")
#username=input("Enter your username: ")
#password=input("Enter your password: ")
#if username==password :
   # print("username and password cant be the same!!")
#elif len(password) < 5 :
    #print("Password too Weak")
#elif 6<= len(password) <12 :
    #print("Password intermediate")
        #playing a game with the comp
# import random

# greet()
# Human=input("Hey welcome to THEE ARENA \n \t Let's play a game with the computer \n \t \t choose between rock,scissor,paper: ").lower()
# Human=Human.strip()
# computer=random.choice(["rock","paper","scissor"])
# if Human not in ["rock","paper","scissor"]:
#     print("Read the instructions carefully")
# elif Human ==computer:
#     print("DRAW!!")
# elif Human =="rock" and computer =="paper" :
#     print("Computer won!! \n Computer's Choice ",computer)
# elif Human =="rock" and computer =="scissor" :
#     print("You won!! \n Computer's Choice ",computer)
# elif Human =="paper" and computer =="rock" :
#     print("You won!! \n Computer's Choice ",computer)
# elif Human =="paper" and computer =="scissor" :
#     print("Computer won!! \n Computer's Choice ",computer)
# elif Human =="scissor" and computer =="rock" :
#     print("Computer won!! \n Computer's Choice ",computer)
# elif Human =="scissor" and computer =="paper" :
#     print("You won!! \n Computer's Choice ",computer)
#greet()
                    #Grade Checker
                    #Take a score (0-100) from the user and print the grade:
# student=input("What's your name? ")
# marks=int(input("Input your marks so that i can give you a Grade \n Pick a number between 0-100: "))
# if marks > 100:
#    print("Choose numbers ranging from 0-100 !!!")
# elif marks >90 <=100:
#    print("A")
# elif marks >80 <=89:
#    print("B")
# elif marks >70 <=79:
#    print("C")
# elif marks >60 <=79:
#    print("D")
# elif marks <60:
#    print("F")
#       Trying if this works diffrenet
#print("Enter your password")
#password=input("Enter your password: ")
#print("What's your username?")
#username=input()
#print("What's your password?")
#password=input()
#if password==username :
 #   print("Username and password can't be the same")
#elif len(password) <=6:
 #   print("password too weak!!")
#elif 6< len(password) <=9 :
 #   print("\tPassword intermediate")
#elif 9< len(password) <=12 :
 #   print("Password strong")
# for i in range(10):
#     print(i)
#     i += 1
# p=98
# kik=90
# print(p/kik)
# WHITE_PAWN = [3,5,6,9]
# row = []
 
# for i in range(8):
#     row.append(WHITE_PAWN)
#     print(row)
# import random
# computer_choice=random.choice(["rock","paper","scissor"])
# human_choice=input("Choose betwwen 'rock' , 'paper' , 'scissor': ").lower
# print(computer_choice)
# if  computer_choice==human_choice:
#     print("DRAW")
# names=input("What's your name?: ")
# age=int(input("What's your Age?: "))
# if age >  18:
#     print("You are eligible to vote!! ",names)
# age=int(input("Enter Your age : "))
# if age < 4:
#     print("The Fee for ",age,"yrs is 2$ ")
# elif age < 18:
#     print("The Fee for ",age,"yrs is 10$ ")
# elif age < 65 :
#     print("The Fee for ",age,"yrs is 35$ ")
# else:
#     print("The Fee for ",age,"yrs is 15$ ")
# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
# Create a variable called alien_color and assign it a value of 'green', 'yellow',
# or 'red'.
# Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points
# alien_color=["green","yellow","red"]
# if 'green' in alien_color:
#     print("You've earned 5 points")
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings: 
    if requested_topping == 'green peppers': 
        print("Sorry, we are out of green peppers right now.") 
    else: 
        print(f"Adding {requested_topping}.") 
print("\nFinished making your pizza!")