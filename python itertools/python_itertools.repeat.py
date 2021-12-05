"""
    itertools.repeat()
"""
from itertools import repeat, cycle

name = 'kevin'

x = repeat(name)

print(next(x))
print(next(x))
print(next(x))
print(next(x))

names = ['kevin', 'john', 'max']

for n in zip(cycle(names), repeat(10, times=10)):
    print(n)
