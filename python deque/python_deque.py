"""
    deque:
         double ended queue
"""

from collections import deque

# d = deque("mohammadhssn")
# x = [10, 20, 30 ,40]

# d.pop()
# d.popleft()         # hazf az aval
#
# d.append(1)
# d.appendleft(2)     # ezafe be aval
#
# print(d.count('m'))

#d.extend(x)
#d.extendleft(x)     # ezafe be avale

# d.rotate(2)         # charkhesh az akhar
# d.rotate(-2)        # charkhesh az aval
#
# print(d)

# -------------------------------------------------------------------------------------------------------------------

# ezafe kardan bishtar az maxlen . be akher ezafe mishe vali az aval list hazf mishe.

# d = deque("mohammadhssn", maxlen=15)
#
# d.append(1)
# d.append(2)
# d.append(3)
# d.append(4)
#
# print(d)