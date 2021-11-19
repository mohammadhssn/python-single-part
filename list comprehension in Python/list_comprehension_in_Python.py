"""
    [output expression forloop if sentence]
"""

# x = []
# for i in range(1,21):
#     x.append(i)
#
# print(x)

# y = [i for i in range(1, 21)]
# print(y)

# ---------------------------------------------------------------------------------------------------------------

# z = [i for i in range(1, 21) if i % 2 == 0]
# print(z)

# ---------------------------------------------------------------------------------------------------------------

# [(1, 'odd'), (2, 'Even')]

# x =[]
#
# for i in range(1,11):
#     if i % 2 == 0:
#         y = i, 'Even'
#         x.append(y)
#     else:
#        y = i, 'odd'
#        x.append(y)
#
# print(x)


# z = [(i, 'Even' if i % 2 == 0 else 'Odd') for i in range(1,11)]
# print(z)


# ---------------------------------------------------------------------------------------------------------------


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)

# newlist = [x for x in fruits if 'a' in x]
# print(newlist)