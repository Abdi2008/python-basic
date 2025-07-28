# x=9
# print(x>3 and x<5)
# for numbers in range(8):
#     print(numbers)
# numbers=list(range(10))
# print(numbers)
# numbers=list(range(3,30,3))   # You can add a third argument which let's python skip the values by the last argument number
# print(numbers[2])
# squares=[]
# for value in range(1,11):
#     squares.append(value*value) #you can either do value*value OR value**2 which ever feasible to you
# print(squares)
# numbers=[100,200,3000,2,9000,4322,211,4,344,87]
# print("The minimum number is: ", min(numbers))
# print("The maximum number is: ", max(numbers))
# print("\tThe sum of the numbers is: ",sum(numbers)) # one can only use + when working with strings only if you are using int and string use ,

            #EXCERCISE
    #4-3. Counting to Twenty
# for number in range(1,21):
#     print(number)
        # 4-4. One Million:
# for numbers in range(1,1000000):
#     print()
    # 4-5. Summing a Million:
# number= range(1,1000000)
# print("The minimum number is: " , min(number))
# print("The maximum number is:" , max(number))
# print("The sum of all number is " , sum(number))
    # 4-6. Odd Numbers: 
# for number in range(1,21,2):
#     print(number)
        # 4-7. Threes: 
# number=[]
# for value in range(3,31):
#     number.append(value**2)
# print(number)
    # 4-8. Cubes:
# for number in range(1,11):
#     print(number**3)
    # 4-9. Cube list Comprehension:
# cubes=[]
# for cube in range(1,11):
#     cubes.append(cube**3)
# print(cubes)
        #SLICING THROUGH A LIST
# Dopamine=["Porn","Tiktok","Instagram","Twitter","Snapchat"]
# print("\t\tHere are my TOP 3 Dopamine friers!!")
# for dop in Dopamine[:3]:
#     print(dop)
        #MAKING TWO SEPARATE COPIES OF LIST USING SLICE
# my_foods=['chicken','pilau','fish']
# friend_food=my_foods[:]     #if you don't use the slice it will make the list same , technically they will become one
# my_foods.append('soldato')
# friend_food.append('ugali')
# print('\tmy favourite foods are: \n',my_foods)
# print("\tmy firend's favourite foods are: \n",friend_food)

        #   quizes  4-10. Slices
# print('The first three items in my list are: ',my_foods[:3]) # or my_foods[0:3]
# print('Three items from the middle of the list are:',my_foods[2:])
# print('The last three items in the list are: ',my_foods[-3:])
        # 4-11. My Pizzas, Your Pizzas: 
# pizzas=["peperonni","chicken","extra-cheese"]
# freind_pizzas=pizzas[:]
# pizzas.append('fish')
# freind_pizzas.append('mushroom')
# pizzas.insert(2,'pineapple')
# print("\t \t Here are my favoutite pizza types: ")
# for piz in pizzas:
#     print(piz)
# print("\t  Here are my friend's favoutite pizza types: ")
# for pizs in freind_pizzas:
#     print(pizs)
my_foods=['chicken','pilau','fish']
friend_food=my_foods[:]     #if you don't use the slice it will make the list same , technically they will become one
my_foods.append('soldato')
friend_food.append('ugali')
print('The first three items in my list are: ')
for thr in my_foods[:3]:
    print(thr) # or my_foods[0:3]
print('Three items from the middle of the list are:')
for th in my_foods[2:]:
    print('\t',th)

print('The last three items in the list are: ')
for tr in my_foods[-3:]:
    print('\t \t',tr)