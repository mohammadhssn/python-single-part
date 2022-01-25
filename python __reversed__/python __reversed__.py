"""
    __reversed__
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __reversed__(self):
        return self.name[::-1]
        # return reversed(self.name)


p = Person('ali', 22)

print(reversed(p))
