"""
    hash() => __hash__
        Return the hash value of the object (if it has one). Hash values are integers.
        They are used to quickly compare dictionary keys during a dictionary lookup.
        Numeric values that compare equal have the same hash value (even if they are of different types,
        as is the case for 1 and 1.0).
"""


# a = "mohammadhssn"
# b = "mohammadhssn"
#
# print(hash(a))
# print(hash(b))

# -------------------------------------------------------------------------------------------------------------------

# # mutable = not hashable
# # immutable = hashable
#
# x = ["ali", 'sara']     # not hashable
#
# y = ('ali', 'sara')     # hashable
#
# #print(hash(x)) # error
# print(hash(y))

# -------------------------------------------------------------------------------------------------------------------

# from collections.abc import Hashable
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __hash__(self):
#         return hash(self.name)
#
#     def __eq__(self, other):
#         if self.name == other.name:
#             return True
#
#
# p1 = Person("sara", 22)
# p2 = Person("mohammadhssn", 24)
#
# # print(hash(p1))
# # print(hash(p2))
#
# print(isinstance(p1, Hashable))
# print(isinstance(p2, Hashable))