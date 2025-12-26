# # def boring_function():
# #     return 123

# # # x = boring_function()
# # boring_function()   #This alone wont print anything.
# # # print("The boring_function has returned its result. It's:", x)
# # def strange_function(n):
# #     n=20
# #     if(n % 2 == 0):
# #         return True
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# test_data = [1900, 2000, 2016, 1987]
# test_results = [True, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"-> ",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year,month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr,mo,"-> ",end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")
def is_prime(num):
    if num % 2 == 0 :
        print("Not Prime")
    elif num %3 ==0:
        print("Not Prime")
    else:
        print("PRIME")
    # Write your code here.
    #
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
