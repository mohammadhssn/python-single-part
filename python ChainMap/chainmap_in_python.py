"""
    ChainMap
"""

from collections import ChainMap

d1 = {'ali': 23, 'sara': 34, 'majid': 55, 'mohammadhssn': 45}
d2 = {'iran': 12, 'mahdi': 76, 'naser': 32}
d3 = {'keyvan': 52, 'ali': 43}

c1 = ChainMap(d1, d2)

print(c1)
print(list(c1.keys()))
print(list(c1.values()))
print(c1.popitem())

c2 = ChainMap(c1.new_child(d3))

print(c1)
print(c2)
