"""
    open/closed principle

    NOTE:
        har class ya method bayad baraye gostaresh open bashe vale braye taghier close bashe.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print('meow')


class Dog(Animal):
    def sound(self):
        print('woof')


class Snake(Animal):
    def sound(self):
        print('hiss')


c1 = Cat('missy')
c1.sound()

d1 = Dog('jack')
d1.sound()

s1 = Snake('sara')
s1.sound()
