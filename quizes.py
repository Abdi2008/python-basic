# # # # # # nums = [1, 2, 3]
# # # # # # vals = nums
# # # # # # del vals[1:2]
# # # # # # print(vals)
# # # # # def fun(x, y, z):
# # # # #     return x + 2 * y + 3 * z


# # # # # print(fun(0, z=1, y=3))

# # # # def fun(inp=2, out=3):
# # # #     return inp * out


# # # # print(fun(out=2))

# # # dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# # # v = dictionary['one']

# # # for k in range(len(dictionary)):
# # #     v = dictionary[v]

# # # print(v)

# # tup = (1, 2, 4, 8)
# # tup = tup[1:-1]
# # tup = tup[0]
# # print(tup)

# try:
#     # Some code is here...
# except:
#     # Some code is here...

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
