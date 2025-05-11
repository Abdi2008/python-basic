#import this #it gives you motivation you need to learn pyhton and how to use it correctly
#bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
#print(bicycles) #python returns all of the list but they have the bracket and strings
#print(bicycles[0]) #python naming convention starts from 0 not 1
#print(bicycles[1])
#print(bicycles[2])
#print(bicycles[3])
#print(bicycles[-1]) #negative one is used to capture the last item on the list this will come in handy when you don't know how long the list is
#print("This was my first bicycle ever: ",bicycles[0]) #you can also use this on a print
#name=["abshir","luul","fowziyo","mohamed","abdirahman","abdullahi","harun","asma","zuhur"]
#message="Hy Welcome "
#print(message+name[0].title())
#print(message+name[1].title())
#print(message+name[2].title())
#print(message+name[3].title())
#print(message+name[4].title())
#print(message+name[-4].title())
#print(message+name[-3].title())
#print(message+name[-2].title())
#print(message+name[-1].title())
#print("i like my mother who's name is ",name[1])
#nganya=["stung","stung2.0","redeemer","givenchy","eschol","space x"]
#print("The best Nganya in Komarock is: ",nganya[1].title())
#nganya.append("Shady")          #Append is used to enter a new element in a list it automatically places the element last value of the list
#nganya.insert(2,"Edge")         #insert let's you choose whichever place you wanna put your element in the list.
#del nganya[7]           #You use the del to remove an element from a list.
#print(nganya)
#popped=nganya.pop(1)    #When you use pop you delete the item from the list but you'll sitll have it. you'll use popped to get the value back
#print(nganya)           #when you use pop alone it removes the last one but you can change the value in the brackets to change the value you want
#print(popped)
#shit_car="givenchy"       #you can assign a variable for the element you wanna delete
#nganya.remove("eschol")     #or you can insert the value straight in the brackets
#print(nganya)
        #excersies 
    #3.4 GUEST LIST
guests=["maryan","mahad","mohamed adan"]
print("Hey ",guests[0]," you are invited to my wedding")
print("Hey ",guests[1]," you are invited to my wedding")
print("Hey ",guests[2]," you are invited to my wedding")
print("Press ok to continue with the code")     #i've added this particular code so that the whole code doesn't show at once , it needs to be more responsive
damn= input().lower()           
if damn == "ok" :   #i need to do some research
    print("aight")
    #a guest said he cant make it so i gotta change him with another person
print("\t \t This guest can't make it: ",guests[2].title()," so i have to find a solution")
del guests[2] #i have deleted the guy who can't make
guests.insert(2,"nasrudin") # i replaced him with another guy using the insert method
print("\t Here's my new updated list ",guests)
print("Hey ",guests[0].title()," you are invited to my wedding")
print("Hey ",guests[1].title()," you are invited to my wedding")        #Here are my new invations for the new list
print("Hey ",guests[2].title()," you are invited to my wedding")
    # 3-6. More Guests: I have to add more guests since the venue of the wedding is changed
print("\t I have to add more guests since the venue of the wedding is changed")
#        Use insert() to add one new guest to the beginning of your list.
#       Use insert() to add one new guest to the middle of your list.
#       Use append() to add one new guest to the end of your list
guests.insert(0,"abdikani")
guests.insert(2,"mudi")
guests.append("ayub")
print("You're invited to the wedding of Mr.Abdirahman Abshir Welcome Mr: ",guests[0].title())
print("You're invited to the wedding of Mr.Abdirahman Abshir Welcome Md: ",guests[1].title())
print("You're invited to the wedding of Mr.Abdirahman Abshir Welcome Mr: ",guests[2].title())
print("You're invited to the wedding of Mr.Abdirahman Abshir Welcome Mr: ",guests[3].title())
print("You're invited to the wedding of Mr.Abdirahman Abshir Welcome Mr: ",guests[4].title())
print("You're invited to the wedding of Mr.Abdirahman Abshir Welcome Mr: ",guests[5].title())
        #3-7. Shrinking Guest List:
print("\t \t \t I CAN ONLY INVITE TWO PEOPLE")
#remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
popped=guests.pop(-1)
print("Hey ",popped," i'm sorry i can't invite you since my bride isn't comfortable with many people")
popped=guests.pop(4)
print("Hey ",popped," i'm sorry i can't invite you since my bride isn't comfortable with many people")
popped=guests.pop(3)
print("Hey ",popped," i'm sorry i can't invite you since my bride isn't comfortable with many people")
popped=guests.pop(0)
print("Hey ",popped," i'm sorry i can't invite you since my bride isn't comfortable with many people")
#       remind the ones who are still invited
print("Hey",guests[0].title()," you're still invited")
print("Hey",guests[1].title()," you're still invited")
        #Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program
del guests[0]
del guests[0]
print(guests,"POV the list is empty")