"""
    meta classes in python
"""


# class A:
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#
#
# a1 = A()

# p1 = type('Person', (), {})  # ejade class ba type
# print(p1)

# --------------------------------------------------------------------------------------------------------------------

# class Singelton(type):
#     _instance = None
#
#     def __call__(self, *args, **kwargs):
#         if self._instance is None:
#             self._instance = super().__call__()
#         return self._instance
#
#
# class Db(metaclass=Singelton):
#     pass
#
# d1= Db()
# d2= Db()
#
# print(id(d1))
# print(id(d2))
