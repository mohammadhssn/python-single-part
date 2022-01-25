"""
    islice
"""

from itertools import islice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = islice(numbers, 2)  # [1, 2]
result_2 = islice(numbers, 2, 8)  # [3, 4, 5, 6, 7, 8]   khode adade 2 shamel nemishe
result_3 = islice(numbers, 2, None)  # [3, 4, 5, 6, 7, 8, 9]   khode adade 2 shamel nemishe
result_4 = islice(numbers, 2, None, 3)  # [3, 4, 5, 6, 7, 8, 9]   (3 == step)

print(list(result))
print(list(result_2))
print(list(result_3))
print(list(result_4))
