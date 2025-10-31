# year=2001
# month=10
# day=21
# print("The date of my official birth is: ")
# print(day,month,year,sep="/")
# john=3
# mary=5
# adam=6
# print(6//6)
# print(john,mary,adam,sep=",")
# total_apples=john+mary+adam
# print("Total Apples:" , total_apples)
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# # find a total of all minutes
# mins=mins + dura
# # find a number of hours hidden in minutes and update the hour
# mins/=60
# # correct minutes to fall in the (0..59) range
# hour+=mins
# # correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# mins = mins + dura # find a total of all minutes
# hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
# mins = mins % 60 # correct minutes to fall in the (0..59) range
# hour = hour % 24 # correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')

# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)
# weather="bad"
# resturant_food="no"
# if weather =="good":
#     if resturant_food=="yes":
#         print("Eat Pasta")
#     else:
#         print("Eat Smocha")
# else:
#     print("The weather is badd")
#     stock="red"
#     print("\tStay at Home")
#     if stock=="green":
#         print("\t\tCook lasagna")
#     else:
#         print("\t\tCook chapati")
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1 > num2 :
#     if num1 > num3:
#         print(num1," num is the greatest".upper())
# elif num2 > num1 :
#     if num2 > num3:
#         print(num2," num2 is the greatest".upper())
# else:
#     print(num3," num3 is the greatest".upper())
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
 
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
 
# largest_number = max(number1, number2, number3)
# smallest_number = min(number1, number2, number3)
 
# # Print the result.
# print("The largest number is:", largest_number)
# print("The smallest number is: ", smallest_number)
# lily="spathiphyllum"
# lily2="pelargonium"
# lily3="Spathiphyllum"
# lily=input("Enter the plant name: \n")
# if lily == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# elif lily == "pelargonium":
#     print("Spathiphyllum! Not pelargonium!")
# elif lily == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# else:
#     print("Invalid choice")
# income = float(input("Enter the annual income: \n"))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# # Write the rest of your code here.
# elif income > 85528:
# 	tax = income * 0.32 - 14839.02
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")
# year=2020
# print(year%4==0)
# year=2021
# if year%4==0 :
#     print("Leap year")
# else:
#     print("common year")
# while True:
#     print("I'm stuck inside a loop.")
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0

# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))

# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))

# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)
# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)
# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# usrinput=int(input("Enter the number: "))
# while secret_number!=usrinput:
#     print("Ha ha! You're stuck in my loop!")
#     usrinput=int(input("Enter the number: "))
# print("\tWell done, muggle! You are free now.")
# import time

# # Write a for loop that counts to five.
# for count in range(1,6):
#     # Body of the loop - print the loop iteration number and the word "Mississippi".
#     print(count," Mississippi")
#     # Body of the loop - use: time.sleep(1)
    
# # Write a print function with the final message.
# print("Ready or not, here I come !")
# break - example

# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")


# # continue - example

# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Enter a number or type -1 to end the program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("The largest number is", largest_number)
#     print("Number of times you entered a number: ",counter)
# else:
#     print("You haven't entered any number.")
# largest_number = -99999999
# counter = 0

# number = int(input("Enter a number or type -1 to end program: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end the program: "))

# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

# while True:
#     word=input("Enter the magic word inorder to exit the loop: ").lower()
#     if word =="chupacabra":
#         break
# print("You've successfully left the loop.")
# user_word = input("Enter a word: ").upper()
# vowels = "AEIOU" # Define all vowels in one string

# for letter in user_word:
#     # Check if the current letter is *in* the string of vowels
#     if letter in vowels:
#         continue # If it's a vowel, skip the rest of this iteration
    
#     # If the code reaches here, the letter is a consonant
#     print(letter)
    #Modify the snippet a bit so that the loop has no chance to execute its body even once:
# i = 6
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)
#Create a for loop that counts from 0 to 10, and prints odd numbers to the screen
# for i in range(11):
#     if i%2==1:
#         print(i," is an ODD NUMBER")
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch,end="")
# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")
# n = 3
 
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)
# n = range(4)
 
# for num in n:
#     print(num - 1)
# else:
#     print(num)
# for i in range(0, 6, 3):
#     print(i)
# i = 1
# j = not not i
# print(i)
# numbers=[1,4,8,99,33,23,12]
# print(numbers)
# print("The total no of values in this variable is: ",len(numbers))
# hat=[1,2,3,4,5]
# num1=int(input("Enter a number: "))
# hat[2]=num1
# del hat[-1]
# print(len(hat))
# print(hat)
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# #
# numbers.insert(1, 333)
# print(numbers)
# my_list = []  # Creating an empty list.
 
# for i in range(5):
#     my_list.insert(0, i + 1)
 
# print(my_list)
# my_list = [10, 1, 8, 3, 5]
# total = 0
 
# for i in my_list:
#     total += i
 
# print(total)
# my_list = [10, 1, 8, 3, 5]
 
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
 
# print(my_list)
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# print(my_list)
# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)
 
# print(lst)
# lst = [1, [2, 3], 4]
# print(lst[1])
# print(len(lst))
# my_list = [32, 40, 10, 21, 9]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
# swaped=0
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             swaped +=1
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print("Number of times a swap happened : ", swaped)
# print(my_list)
    #An Easier way 
# my_li=[1,67,5,3,87,9,3,2,2,4,5,67,87]
# my_li.sort()
# my_li.reverse() # you use them together inorder to get the numbers decsending
# print(my_li)
banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie' 
if user  not in banned_users: # not in and in can be used to check if a value is in a list
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print("Nahh Chop basto")