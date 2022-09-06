"""
    python_functools_single_dispatch:
        The singledispatch decorator belongs to the functools module and was added in Python version 3.4.
        The singledispatch decorator is used to convert the function into a public function that can have different -
         behaviors depending on the type of the first argument.

    NOTE:
        The function on which the singledispatch decorator is used is set as the default function, and
         you can implement other functions by using register.
         If the functions specified by register do not handle the input data type, the default function will be executed
"""

from functools import singledispatch


@singledispatch
def show(data):
    raise NotImplementedError('Unsupported data!')


@show.register(str)
@show.register(list)
def _(data):
    for d in data:
        print(d)


@show.register
def _(data: int):
    print(data * 2)


# show('mohammadhssn')
# show([1, 2, 3])
#
# show(12)  # 24
# show({'key': 'value'})  # NotImplementedError

print(show.registry)  # {<class 'object'>: <function show at 0x7f4060e6fd90>, <class 'list'>: <function _ at 0x7f4060c90670>, <class 'str'>: <function _ at 0x7f4060c90670>, <class 'int'>: <function _ at 0x7f4060c90550>}
print(show.dispatch(int))   # <function _ at 0x7f7cb966c5e0>
