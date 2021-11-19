# class A:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, name, *args, **kwargs):
#         if name == "ali":
#             return None
#         else:
#             return super().__new__(cls, *args, **kwargs)
#
#
# a1 = A("ali")
# print(a1)
#
