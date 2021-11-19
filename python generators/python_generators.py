"""
    Generators => 1. Function  2. Expression(comprehension)
"""

# 1. Function

#
# def Show(num):
#     print("Starting...")
#     while num > 0:
#         yield num
#         num -= 1


# for i in Show(5):
#     print(i)

# s = Show(5)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# ---------------------------------------------------------------------------------------------------------------

# 2. Expression(comprehension)

# evenNumber = (i for i in range(1, 11) if i % 2 == 0)
# showNumbers = (i for i in range(1, 101))

# print(next(evenNumber))
# print(next(evenNumber))
# print(next(showNumbers))
# print(next(showNumbers))
