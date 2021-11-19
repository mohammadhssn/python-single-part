"""
    enum:
        An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration,
         the members can be compared by identity, and the enumeration itself can be iterated over.
"""
import enum as en


# @en.unique  # maghadir tekrari mojaz nist
# class Days(en.Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#     # Sun = 2 # Error
#     # Www = 2  # Error
#
#
# print(Days.Fri.name)
# print(Days.Fri.value)
# print(repr(Days.Wed))
# print(Days(2))

# -----------------------------------------------------------------------------------------------------------------

# @en.unique  # maghadir tekrari mojaz nist
# class Days(en.Enum):
#     Sun = en.auto()
#     Mon = en.auto()
#     Tue = en.auto()
#     Wed = en.auto()
#     Thu = en.auto()
#     Fri = en.auto()
#     Sat = en.auto()


# for day in Days:
#     print(day.name, day.value)
#
#
# for day, val in Days.__members__.items():
#     print(day, val.value)

# print(Days.Fri == Days.Wed)
# # print(Days.Wed > Days.Thu) # Error

# -----------------------------------------------------------------------------------------------------------------

# @en.unique  # maghadir tekrari mojaz nist
# class Days(en.IntEnum): # IntEnum
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6


# print(Days.Sun > Days.Thu)
