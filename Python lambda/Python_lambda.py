"""
    lambda (arguments): manipulation(arguments)
"""

# def Add(x,y):
#     return x + y

# Add = lambda x, y: x + y      #lambda
#
# print(Add(3, 5))

# --------------------------------------------------------------------------------------------------------------------

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def Multi(i):
#     return i * i
# print(list(map(Multi, x)))

# print(list(map(lambda i:i*i, x)))   #lambda

# --------------------------------------------------------------------------------------------------------------------

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def Even(i):
#     if i % 2 == 0:
#         return True
#     return False
#
#
# # print(list(filter(Even,x)))
#
# print(list(filter(lambda i: i % 2 == 0, x)))  # lambda

# --------------------------------------------------------------------------------------------------------------------

# x = [(2,'e'), (4, 't'), (6, 'b'), (1, 'a'), (3, 'c')]
#
# # print(sorted(x))
# print(sorted(x, key=lambda i:i[1]))     #lambda
