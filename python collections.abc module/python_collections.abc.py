"""
    collections.abc
"""

from collections.abc import Sequence, Sized, Container


# Sequence

def add(arg1):
    if isinstance(arg1, Sequence):
        print('Yes')
    else:
        print('No')


add(1)  # No
add([1, 2, 3])  # Yes


# Container

class Person:

    def __contains__(self, item):
        pass


print(issubclass(Person, Container))  # True


# Sized

class A:
    def __len__(self):
        return 2


a = A()

print(isinstance(a, Sized))  # True
