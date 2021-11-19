"""
    1. functions are objects.
    2. functions can be stored in data structure.
    3. functions can be passed to other functions (higher-order functions).
    4. functions can be nested (inner and outer functions).
    5. functions can capture local state (lexical closure).
    6. objects can behave like functions.
"""

# -------------------------------------------------------------------------------------------------------------------


# 1. functions are objects.

# def Show(name):
#     return f"Hello {name}"
#
#
# f = Show
# print(f("mohammadhssn"))


# -------------------------------------------------------------------------------------------------------------------


# 2. functions can be stored in data structure.

# def Show(name):
#     return f"hello {name.upper()}"
#
#
# x = [Show, str.capitalize, str.lower]
#
# for i in x:
#     print(i("mohammadhssn"))
#
# print(x[1]("ali"))

# -------------------------------------------------------------------------------------------------------------------

# 3. functions can be passed to other functions (higher-order functions).

# def Show(name):
#     return f'Hello {name}'
#
#
# def Shoot(func, name):
#     return func(name)
#
#
# print(Shoot(Show, "mohammadhssn"))
#
# for i in map(Show, ["ali", "reza", "sara"]):
#     print(i)

# -------------------------------------------------------------------------------------------------------------------

# 4. functions can be nested (inner and outer functions).

# def Person(age):
#     def Adult(name):
#         return f"{name} is Adult."
#
#     def Kid(name):
#         return f"{name} is kid."
#
#     if age >= 18:
#         return Adult
#     else:
#         return Kid
#
#
# p = Person(10)
# print(p("mohammadhssn"))

# -------------------------------------------------------------------------------------------------------------------

# 5. functions can capture local state (lexical closure).

# def Person(age, name):
#     def Adult():
#         return f"{name} is Adult."
#
#     def Kid():
#         return f"{name} is Kid."
#
#     if age >= 18:
#         return Adult
#     else:
#         return Kid
#
#
# print(Person(20, "mohammadhssn")())

# -------------------------------------------------------------------------------------------------------------------

# 6. objects can behave like functions.


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __call__(self, *args, **kwargs):
#         print(f"{self.name} is {self.age} year old.")
#
# p1 = Person("mohammadhssn", 30)
# p1()
