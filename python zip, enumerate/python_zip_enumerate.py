"""
    zip(), enumerate()
"""

names = ['sara', 'ali', 'mohammadhssn', 'milad']
scores = [10, 30, 4, 22, 39]

for n, s in zip(names, scores):
    print(f'{n} == {s}')

print(list(zip(names, scores)))  # scores(39) is removed

# enumerate

for i, n in enumerate(names):
    print(f'{i} == {n}')
