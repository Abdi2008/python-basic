                                #Ask the user for a number. Print whether it’s even or odd.
#number1 = int(input("Choose a number: "))
#if number1 %2==0:
    #print("Number is even")
#else:
    #print("Number is Odd")
#score=int(input("Hey i want you to input your Mean Grade for this sem: "))
#if 90<= score <= 100 :
 #   print("Wonderful Acheivement")
#elif 80<= score <= 89 :
 #   print("Lovely stuff")
#elif 70<= score <= 79 :
 #   print("Great Work")
#elif score > 100:
 #   print("Read the manuals well")
#elif 60<= score <=79 :
 #   print("PASS")
#else:
  #  print("You are a fraud")
                                        #Input someone's age and determine their group:
#age=int(input("Hey i want you to input your age here: "))
#if  age <=12 :
 #   print("You're a Child")
#elif 13<= age <=17 :
 #   print("You're a Teen")
#elif 18<= age <=64 :
 #   print("You are an Adult")
#else :
   # print ("you are a Senior")
#username=input("What's your username? ")
#password= input("What's your Password? ")
#if username == password:
 #   print("Password and username can't be the same!!!!")
#elif len(password) < 6 :
 #   print("Password too weak")
#elif 6 <= len(password) <= 9 :
 #   print("Password Moderate")
#elif len(password) > 9 :
    #print("Password Strong")
#leap=int(input("Enter a year so that you check if it's a leap year or not: "))
#if leap%4 == 0:
 #   print("Leap Year")
#else:
   # print("Not a leap year")
                #Largest of 3 Numbers
#num1=int(input("I want you to input three numbers, this one is the first: "))
#num2=int(input("2nd number...: "))
#num3=int(input("3rd number....: "))
#if num1 > num2 and num1 > num3 :
 #   print ("1st Number is the Greatest")
#elif num2>num1 and num2 > num3 :
 #   print("2nd number is the Greatest")
#else:
 #   print("3rd number is the Greatest")
            #play rock paper scissors with the computer.
import random
Abdi=input("You'll be playing a game with the computer \n choose between Rock,Paper,Scissor: ").lower()
comp=random.choice(["rock","paper","scissor"])
if Abdi==comp:
    print("DRAW")
elif Abdi=="rock" and comp =="scisssor":
    print("Abdi Congratulation\n The computer's schoice : ",comp)
elif Abdi=="rock" and comp =="paper":
    print("Abdi you lost\n The computer's schoice : ",comp)
elif Abdi=="paper" and comp =="scisssor":
    print("Abdi you lost\n The computer's schoice : ",comp)
elif Abdi=="paper" and comp =="rock":
    print("Abdi Congratulation\n The computer's schoice : ",comp)
elif Abdi=="scissor" and comp =="rock":
    print("Abdi you lost\n The computer's schoice : ",comp)
elif Abdi=="scissor" and comp =="paper":
    print("Abdi Congratulation\n The computer's schoice : ",comp)