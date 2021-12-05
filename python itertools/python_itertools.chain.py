"""
    itertools.chain(), chain.from_iterable()
"""
from itertools import chain

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8]

print(list(chain(odds, evens)))

name = 'sara'

print(list(chain.from_iterable(name)))
