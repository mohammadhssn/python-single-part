"""
    python class variables evaluate on declaration/import
"""


class A:
    def __init__(self):
        print('This is from class A')


class B:
    a = A()
