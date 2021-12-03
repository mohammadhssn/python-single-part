"""
    Single responsibility principle

    NOTE:
        har class ya method faghat masoule yek kar bashe,
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f'{self.name} is {self.age} years old'


class Db:
    def save_db(self):
        pass


p1 = Person('mohammadhssn', 22)
