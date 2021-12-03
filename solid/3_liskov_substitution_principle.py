"""
    liskov substitution principle

    NOTE:
        age ye class dashte bashim va az oon chand object ejad karde bashim . age jaye objetc haro ba ham avaz konim
        nabayad barname dochare moshkel beshe.
"""


class Bird:
    def __init__(self, name):
        self.name = name


class FlyingBird(Bird):
    def fly(self):
        print(f'{self.name} is flying')


b1 = Bird('penguin')
b2 = FlyingBird('eagle')
b2.fly()
