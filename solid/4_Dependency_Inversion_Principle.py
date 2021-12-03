"""
    Dependency Inversion Principle
"""


class IFood:
    def bake(self):
        pass

    def eat(self):
        pass


class Bread(IFood):
    def bake(self):
        print('Bread was baking')

    def eat(self):
        print('Bread was eaten')


class Pastry(IFood):
    def bake(self):
        print('Pastry was baking')

    def eat(self):
        print('Pastry was eaten')


class Production:
    def __init__(self, food):
        self.food = food

    def produce(self):
        self.food.bake()

    def consume(self):
        self.food.eat()


produceBread = Production(Bread())
produceBread.produce()
produceBread.consume()
producePastry = Production(Pastry())
producePastry.produce()
producePastry.consume()
