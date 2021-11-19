"""
    creating iterable objects
        __iter__. __next__
"""

# class A:
#     def __init__(self, value):
#         self.value = value
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.value:
#             current = self.current
#             self.current += 1
#             return current
#         raise StopIteration
#
#
# a1 = A(15)
# for i in a1:
#     print(i)
