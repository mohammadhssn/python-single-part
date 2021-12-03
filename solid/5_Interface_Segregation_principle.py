"""
    Interface Segregation principle

    NOTE:
        be jaye ejade ye class bozorg va base ke ghare baghie class ha az oon ers bary konan
        biyaym ye az yek ya chand class koochekter estefade konim.
"""

from abc import ABC


class Shape(ABC):
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass
