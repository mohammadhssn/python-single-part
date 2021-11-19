
# a = [1, 2, 3, 4, 5, 6]
#
# b = a                   #Shallow Copy
# b[0] = 11
#
# print(id(a))
# print(id(b))
# print(a)
# print(b)



# -------------------------------------------------------------------------------------------------------------------

# # list(), set(), dict()
#
# a = [1, 2, 3, 4, 5, 6]
#
# b = list(a)             #Deep Copy
# b[0] = 11
#
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# -------------------------------------------------------------------------------------------------------------------

# list(), set(), dict() To Object hay TOdarTO Kar nemikonan Shallow Copy migiran

# a = [1, 2, 3, 4, 5, 6, [7, 8]]
#
# b = list(a)             #Shallow Copy
# b[6][0] = 777
#
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# -------------------------------------------------------------------------------------------------------------------

# from copy import deepcopy
#
# a = [1, 2, 3, 4, 5, 6, [7, 8]]
#
# b = deepcopy(a)             #Deep Copy
# b[6][0] = 777
#
# print(id(a))
# print(id(b))
# print(a)
# print(b)