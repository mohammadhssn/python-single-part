"""
    map() - filter() - reduce()
"""

# reduce
from functools import reduce

numbers = [1, 4, 65, 3]


def add(a, b):
    return a + b


print(reduce(add, numbers))  # 73
print(reduce(add, numbers, 10))  # 83

# map
names = ['sara', 'ali', 'mohammadhssn']


def show(name):
    return f'welcome {name}'


print(list(map(show, names)))

# filter
ages = [23, 12, 54, 32]


def age_show(age):
    if age >= 18:
        return True


print(list(filter(age_show, ages)))
