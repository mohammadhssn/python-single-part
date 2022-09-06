"""
    python-missing:
        Python's __missing__ method specifies the behavior of a dictionary when calling a key that does not exist.
         More specifically, if you request a key in a dictionary that does not exist,
          the __getitem__ method will call the __missing__ method.
        The value you return to the __missing__ method will replace the KeyError error.
"""


class MyDict(dict):
    def __missing__(self, key):
        return f'default_value for {key}'


users = MyDict({'sara': 25, 'ali': 20})
print(users['sara'])  # 25
print(users['ali'])  # 20
print(users['mohammadhssn'])  # default_value for mohammadhssn
