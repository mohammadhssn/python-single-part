"""
    itertools.accumulate()
"""
from itertools import accumulate
import operator

numbers = [1, 3, 5, 66, 3, 4, 56]

print(list(accumulate(numbers, initial=100)))

print(list(accumulate(numbers, func=operator.sub)))
