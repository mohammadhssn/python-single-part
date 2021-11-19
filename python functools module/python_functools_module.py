"""
    functools => partial - update_wrapper
"""

# from functools import partial, update_wrapper
#
#
# def multi(x, y):
#     """
#     Multi Function
#     :param x:
#     :param y:
#     :return:
#     """
#     return x * y


# def double(x):
#     return x * 2
#
#
# def triple(x):
#     return x * 3


# double = partial(multi, y=2)
# triple = partial(multi, y=3)

# print(double(3))
# print(triple(3))
# print(double.__name__)  #error
# print(double.__doc__)   #error


# -----------

# update_wrapper(double, multi)
# update_wrapper(triple, multi)
#
# print(double.__name__)
# print(double.__doc__)
# print('----------------------------------')
# print(triple.__name__)
# print(triple.__doc__)
