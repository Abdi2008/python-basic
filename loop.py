#we start our lessons of looping .
        #for loop
# magicians=["Darly","Risa","Sinda","Peter","Griffin","Lisa","Simba","Reece"]
# for magician in magicians:
#     print("Hey "+magician.title()+", that was awesome magic tricks")
#     print("I can't wait to see your next tricks my friend "+magician.lower())
# print("Thanks to all the magicians who particpated in this show")
# pizzas=["peperonni","chicken","extra-cheese"]
# for pizza in pizzas:
#     print(pizza.title())
#     print("I really love "+pizza.title()+" when it is served HOT")
# print("\t\t i really love Pizzas")
# animals=["dog","cat","wolf","horse"]
# for animal in animals:
#     print(animal)
#     print("A "+animal.title()+" can make a great companion")
# print("\tThese animals are my favourites")
# EMPTY = []
# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
# print(board)
# numb=10
# num=0
# sum=0
# while num < numb:
#     print("Numb is greater "+ str(num))
#     sum +=num
#     num +=1
# print(sum)
# def looping():
#     aws_services=["S3","LAMBDA","EC2","RDS","DynamoDB"]
#     print(f"The AWS SERVICES ARE: {aws_services}")

# #Use a FOR LOOP To Iliterate through the list.
#     for service in aws_services:
#         print(f"Using a for loop to list the services: {service}")
#     service=0
#     print("\n")
#     while service <= len(aws_services)-1:
#         print(f"Using a while loop to list the services: {aws_services[service]}")
#         service+=1
#     # print("\nUsing a While loop to seive through the list")
#     # index= len(aws_services)-1
#     # while index >0 :
#     #     print(f"Aws Services {aws_services[index]}")
#     #     index-=1
# looping()
# import boto3
# calls=0
# while calls<0:
#     calls+=1
# print(calls)
i=1
sum=0
while i <=4:
    sum+=i
    i+=1
print(sum)