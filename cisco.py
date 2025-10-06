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
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')