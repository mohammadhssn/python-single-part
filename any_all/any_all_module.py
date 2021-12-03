"""
    any() - all()
"""

obj1 = [1, False, '']

print(any(obj1))

obj2 = [2, True, 'a']
print(all(obj2))

obj3 = ''
print(any(obj3))

obj4 = 'good'
print(any(obj4))

obj5 = ''
print(all(obj5))

obj6 = {'name': 'ali', 'married': True}
print(any(obj6))

obj7 = {'name': 'ali', 'married': True}
print(all(obj7))
