"""
    comparison methods:
        __lt__  =>  lower than       x < y
        __le__  =>  lower equal      x <= y
        __eq__  =>  equal            x == y
        __ne__  =>  not equal        x != y     x <> y
        __gt__  =>  greater than     x > y
        __ge__  =>  greater equal    x >= y
"""


# class Human:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.name == other.name and self.age == other.age
#         return False
#
#     def __ne__(self, other):
#         return self.name != other.name or self.age != other.age
#
#
# class Alien:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.name == other.name and self.age == other.age
#         return False
#
#     def __ne__(self, other):
#         return self.name != other.name or self.age != other.age
#
#
# h1 = Human("jack", 12)
# h2 = Human("jack", 12)
# a1 = Alien("jack", 12)
#
# print(h1 == h2)   # True
# print(h1 != h2)   # False
# print(a1 == h1)     # False  Run __eq__ class Alien
# print(h1 == a1)     # False  Run __eq__ class Human
