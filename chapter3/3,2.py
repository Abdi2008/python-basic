#cars="posche","g-wagon","ferari","fortuner","hilux","alto","mercedes" # list of cars
#cars.sorted()
#print("Total Number of cars: ",len(cars))
#print(sorted(cars))
        # My Top Vacation Spots i would like to go
#vaca=["malaysia","thailand","zanzibar","cape of good hope","marakech","diani","china"]
#print(vaca)         #print the list in it's raw form
#print(sorted(vaca))     # use sorted to modify the list in alphabeticall order temporarily
#print(vaca)         #show the list if it's still unchanged
#print(sorted(vaca,reverse=True))    #print the list in reverse order temporarily
#print(vaca) #see if the list is working as usuall
#vaca.reverse()      #use reverse to change the cars permanently
#print(vaca)
#vaca.reverse()      #use reverse to repeat the list as it was
#print(vaca)     #check if it's working
#vaca.sort()     #use sort to permnanently to change the list
#print(vaca)
#vaca.sort(reverse=True)     #use sort reverse to change the list permanently
#print(vaca)
#        Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities,
#languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once
countries=["Somalia","Kenya","Morocco","Palestine","Turkey","Congo","Indonesia","Brazil","Malaysia","Portugal"]  #countries i like
print(countries)
pss=countries.pop(5)
print("This country is facing major internal and external fight because it's richh richh \n Her name is: ",pss) 
print(countries) #Congo just dissaperad but it's cool we stored it in a variable
    #i wanna delete a country because i have mixed signals with it
del countries[-1]
print(countries)
            #i wanna add a country which i forgot to add
countries.insert(8,"Tanzania")
countries.insert(3,"Madagascar")
countries.insert(2,"Sychelles")
countries.append("Bali")
print(countries)
#print(countries[12])        #intentional Error
print(countries[11])        # rectifying the mistake
print(sorted(countries))    #listing the list in alphabeticall order.
print("List of countries i would like to visit in my lifetime; ",len(countries)) #counting the number of countries