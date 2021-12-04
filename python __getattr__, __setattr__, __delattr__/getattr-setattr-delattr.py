"""
    __getattr()__, __setattr__(), __delattr__(), __getattribute__()
"""


class Person:
    name = 'mohammadhssn'
    email = 'm@email.com'

    def __getattr__(self, item):
        if item == 'age':
            return f'{item} dose not exists!'
        return super().__getattr__(item)

    def __getattribute__(self, item):
        if item == 'name':
            return 'cant access to name'
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key == 'city':
            print('cant create attribute city')
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'email':
            return 'cant delete email'
        return super().__delattr__(item)


p1 = Person()
print(p1.age)           # age dose not exists!
print(p1.name)          # cant access to name
p1.city = 'shahrood'    # cant create attribute city
del p1.email            # cant delete email
print(p1.email)         # 'm@email.com'
