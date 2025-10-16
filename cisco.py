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
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

