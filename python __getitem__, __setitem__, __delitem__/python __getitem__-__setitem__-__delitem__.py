"""
    getitem(), setitem(), delitem()
"""


class MyList:
    def __init__(self, element=1):
        self.my_list = [None] * element

    def __str__(self):
        return str(list(self.my_list))

    def __setitem__(self, key, value):
        self.my_list[key] = value

    def __getitem__(self, item):
        return self.my_list[item]

    def __delitem__(self, key):
        self.my_list[key] = None


m = MyList(6)
m[0] = 00
m[1] = 11
m[2] = 22
m[3] = 33
m[4] = 44
m[5] = 55
print(m)
del m[5]
print(m[5])  # None
print(m[5])  # None
