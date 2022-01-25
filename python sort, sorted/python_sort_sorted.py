"""
    sort(), sorted()
"""

# sorted()  ye object iterable migire va khooroji ye list jadid barmigardoone.


names = ['ali', 'sara', 'amirali', 'kevin', 'mohammadhssn']
numbers = [1, 44, 3, 55, 4]

names2 = sorted(names)
names3 = sorted(names, key=len)
numbers2 = sorted(numbers)
numbers3 = sorted(numbers, reverse=True)

print(names2)
print(names3)
print(numbers2)
print(numbers3)

# sort()   faghat rooye list emal mishe va list asli ro tagir mide.

ages = [22, 33, 21, 2, 44, 53, 14]

print(ages)
ages.sort()
print(ages)
