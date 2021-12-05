"""
    itertools.count()
"""

from itertools import count

n = map(lambda x: x ** 2, count(0, 1))

for i in n:
    if i > 100:
        break
    print(i)

names = ['sara', 'kevin', 'mork']

for i in zip(count(0, 1), names):
    print(i)
