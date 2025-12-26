# def boring_function():
#     return 123

# # x = boring_function()
# boring_function()   #This alone wont print anything.
# # print("The boring_function has returned its result. It's:", x)
# def strange_function(n):
#     n=20
#     if(n % 2 == 0):
#         return True
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [True, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
