"""
    inheriting python built objects:
        When coding in Python, you may need to create classes that behave like internal Python objects.
        For example, you need a class that works like Python lists.
        Instead of wasting your time on implementing such a class, you can inherit from Python's internal objects.

    NOTE:
        1: In order to inherit from Python's internal objects,
            you must be completely familiar with that object and know its behavior.

        2: Be sure to write unittest for your codes,
            because changing the behavior of Python's internal objects can cause many problems.
"""


class StringList(list):
    def append(self, element):
        if not isinstance(element, str):
            raise TypeError('This class only accepts stings.')

        return super().append(element)


string_list = StringList()
string_list.append('a')
string_list.append('b')

print(string_list)  # ['a', 'b']

string_list.append(2)  # TypeError: This class only accepts stings.
