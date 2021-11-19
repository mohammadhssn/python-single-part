"""
    Python Decorators:
        1. Creating Decorators.
        2. Applying Multiple Decorator to a Single Function.
        3. Accepting Arguments in Decorator Function.
        4. Defining General Purpose Decorators.
        5. passing Arguments to the Decorator.
        6. Debugging Decorators.

"""

# 1. Creating Decorators.

# def Outer_Upper(func):
#     def Inner_Upper():
#         f = func()
#         text = f.upper()
#         return text
#
#     return Inner_Upper
#
#
# @Outer_Upper
# def Show():
#     return "Hello World"
#
#
# print(Show())

# ---------------------------------------------------------------------------------------------------------------------


# 2. Applying Multiple Decorator to a Single Function.

# def Outer_Upper(func):
#     def Inner_Upper():
#         f = func()
#         text = f.upper()
#         return text
#
#     return Inner_Upper
#
#
# def Outer_Split(func):
#     def Inner_Split():
#         f = func()
#         text = f.split(" ")
#         return text
#
#     return Inner_Split
#
#
# @Outer_Split
# @Outer_Upper
# def Show():
#     return "Hello World"
#
#
# print(Show())

# ---------------------------------------------------------------------------------------------------------------------

# 3. Accepting Arguments in Decorator Function.

# def Outer_Upper(func):
#     def Inner_Upper(t):
#         f = func(t)
#         text = f.upper()
#         return text
#
#     return Inner_Upper
#
#
# @Outer_Upper
# def Show(text):
#     return text
#
#
# print(Show("hello mohammadhssn"))


# ---------------------------------------------------------------------------------------------------------------------

# 4. Defining General Purpose Decorators.

# def Outer_Upper(func):
#     def Inner_Upper(t, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         f = func(t)
#         text = f.upper()
#         return text
#
#     return Inner_Upper
#
#
# @Outer_Upper
# def Show(text):
#     return text
#
#
# print(Show("hello mohammadhssn", "how are you", age = 21))


# ---------------------------------------------------------------------------------------------------------------------


# 5. passing Arguments to the Decorator.

# def Outer_Deco(lname, fname):
#     def Outer_Upper(func):
#         def Inner_Upper(t):
#             print(lname, fname)
#             f = func(t)
#             text = f.upper()
#             return text
#
#         return Inner_Upper
#     return Outer_Upper
#
#
# @Outer_Deco("mohammadhssn", "ALizadeh")
# def Show(text):
#     return text
#
#
# print(Show("how are you"))

# ---------------------------------------------------------------------------------------------------------------------

# 6. Debugging Decorators.

# import functools
#
#
# def Outer_Upper(func):
#     @functools.wraps(func)
#     def Inner_Upper(t):
#         'Doc inner function'
#         f = func(t)
#         text = f.upper()
#         return text
#
#     return Inner_Upper
#
#
# @Outer_Upper
# def Show(text):
#     'Show function'
#     return text
#
#
# print(Show.__name__)
# print(Show.__doc__)
