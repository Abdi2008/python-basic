def greet():
    print("welcome")
#username=input("Enter your username: ")
#password=input("Enter your password: ")
#if username==password :
   # print("username and password cant be the same!!")
#elif len(password) < 5 :
    #print("Password too Weak")
#elif 6<= len(password) <12 :
    #print("Password intermediate")
        #playing a game with the comp
import random


Human=input("Hey welcome to THEE ARENA \n Let's play a game with the computer \n choose between rock,scissor,paper: ").lower()
computer=random.choice(["rock","paper","scissor"])
if Human not in ["rock","paper","scissor"]:
    print("Read the instructions carefully")
elif Human ==computer:
    print("DRAW!!")
elif Human =="rock" and computer =="paper" :
    print("Computer won!! \n Computer's Choice ",computer)
elif Human =="rock" and computer =="scissor" :
    print("You won!! \n Computer's Choice ",computer)
elif Human =="paper" and computer =="rock" :
    print("You won!! \n Computer's Choice ",computer)
elif Human =="paper" and computer =="scissor" :
    print("Computer won!! \n Computer's Choice ",computer)
elif Human =="scissor" and computer =="rock" :
    print("Computer won!! \n Computer's Choice ",computer)
elif Human =="scissor" and computer =="paper" :
    print("You won!! \n Computer's Choice ",computer)
greet()