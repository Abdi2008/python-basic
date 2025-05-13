#cars="posche","g-wagon","ferari","fortuner","hilux","alto","mercedes" # list of cars
#cars.sorted()
#print("Total Number of cars: ",len(cars))
#print(sorted(cars))
        # My Top Vacation Spots i would like to go
vaca=["malaysia","thailand","zanzibar","cape of good hope","marakech","diani","china"]
print(vaca)         #print the list in it's raw form
print(sorted(vaca))     # use sorted to modify the list in alphabeticall order temporarily
print(vaca)         #show the list if it's still unchanged
print(sorted(vaca,reverse=True))    #print the list in reverse order temporarily
print(vaca) #see if the list is working as usuall
vaca.reverse()      #use reverse to change the cars permanently
print(vaca)
vaca.reverse()      #use reverse to repeat the list as it was
print(vaca)     #check if it's working
vaca.sort()     #use sort to permnanently to change the list
print(vaca)
vaca.sort(reverse=True)     #use sort reverse to change the list permanently
print(vaca)