"""
    itertools.compress()
"""
from itertools import compress

names = ['sara', 'kevin', 'mohammdhssn', 'ali']

selectors = [False, True, True, False]

for result in compress(names, selectors):
    print(result)
