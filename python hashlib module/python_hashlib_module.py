"""
    hashlib:
        algorithms_available, algorithms_guaranteed
        update(), hexdigest()
"""
import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

h = hashlib.sha256()

name = 'my name is mohammadhssn'.encode()

h.update(name)

result = h.hexdigest()
print(result)
