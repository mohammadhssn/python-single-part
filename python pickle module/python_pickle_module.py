"""
    pickle
"""

import pickle

# person = {'name': 'sara', 'age': '25'}

# result = pickle.dumps(person)
#
# l_result = pickle.loads(result)
# print(l_result)

# with open('data.pickle', 'wb') as f:
#     pickle.dump(person, f)

with open('data.pickle', 'rb') as f:
    result = pickle.load(f)
print(result)
