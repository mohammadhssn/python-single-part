"""
    isinstance() - issubclass()
"""

name = 'sara'

print(isinstance(name, str))
print(isinstance(name, (list, tuple, bool, str, int)))


class A: pass


a = A()


class B(str): pass


b = B()

print(isinstance(a, A))
print(isinstance(b, B))
print(isinstance(b, str))


# issubclss

class A(str): pass


class B(A): pass


print(issubclass(B, A))
print(issubclass(B, str))
