"""
    contextlib
"""

import contextlib


# tabdile function be contextManger

# @contextlib.contextmanager
# def Show():
#     print("starting...")  # __enter__
#
#     yield {}    # meghdari ke dakhel as (name delkhah) ghara migire.
#
#     print("Ending...")  # __exit__
#
#
# with Show() as s:
#     print('hello')
#
#
# -------------------------------------------------------------------------------------------------------------------

# @contextlib.contextmanager
# def Show(name):
#     print("starting...", name)  # __enter__
#
#     yield {}    # meghdari ke dakhel as (name delkhah) ghara migire.
#
#     print("Ending...", name)  # __exit__
#
#
# with Show("mohammadhssn") as s, Show("sara") as a, Show("majid") as b:
#     print('hello')

# -------------------------------------------------------------------------------------------------------------------

# from urllib.request import urlopen
#
# with contextlib.closing(urlopen("https://www.mongard.ir/")) as m: # contextlib.closing() bad az kar be to khodkar close mokone
#     for i in m:
#         print(i)

# -------------------------------------------------------------------------------------------------------------------

# tabdile class be decorator

# class Cnt(contextlib.ContextDecorator):
#
#     def __enter__(self):
#         print("starting...")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Ending,,,")
#
#
# @Cnt()
# def Show():
#     print("hello")
#
#
# Show()
