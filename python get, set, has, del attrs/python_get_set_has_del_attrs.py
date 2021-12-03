"""
    hasattr(), getattr(), setattr(), delattr()
"""


class Person:
    name = 'mohammadhssn'
    age = 22


print(hasattr(Person, 'age'))  # True
print(hasattr(Person, 'address'))  # False

print(getattr(Person, 'name'))  # mohammadhssn
# print(getattr(Person, 'city'))    # AttributeError

print(setattr(Person, 'city', 'Shahrood'))
print(getattr(Person, 'city'))  # Shahrood

delattr(Person, 'age')
# print(getattr(Person, 'age'))     # AttributeError
