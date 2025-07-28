#A tupple doesn't change like a list
# my_cars=('Volswagen','Ford Raptor')
# my_cars[0]='Chevrolet'
# print(my_cars)
    #RESTURANT BASICS
menu_basic=('tea','coffee','ugali','rice','chapati')
#menu_basic[2]='chicken' #Trying to see if we can modify it but python will reject
print("\tHERE ARE THE MENU BASIC IN EVERY RESTURANT!")
for basic in menu_basic:
    print(basic.title())
menu_basic=('tea','fish','chips','rice','chapati')  #The resturant has decided to change some few foods
print("\t \t HERE IS THE NEW UPDATED MENU:")
for basics in menu_basic:
    print(basics.title())