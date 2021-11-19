# from textwrap import *
#
# s = """
#     Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules,
#     functions, classes, and methods. It's specified in source code that is used, like a comment,
#     to document a specific segment of code.
# """

# print(wrap(s, width=80))   # jomle ro be meghdare (width) mishkane va be soorat list bar migardoone (default = 70).

# -------------------------------------------------------------------------------------------------------------------

# print(fill(s, width=80))   # jomle ro be meghdare (width) - arze matn ro taghir mide (default = 70).

# -------------------------------------------------------------------------------------------------------------------

# print(shorten(s, width=70, placeholder="'Continue >>>'"))  # be meghdare (width) faghat matn ro neshoon mide

# -------------------------------------------------------------------------------------------------------------------

# print(dedent(s)) # tooraftegi ro hazf mikone

# -------------------------------------------------------------------------------------------------------------------

# print(indent(s, prefix="> ")) # meghdare (prefix) ro har ja ke tooraftegi dashte bashim ghara mide

# -------------------------------------------------------------------------------------------------------------------

# # TextWrapper   #age behkaym chandin option dashe bashim az TextWrapper estefade mikonim.
# # expand_tabs   # dar matnemoon Tab ro neshoon bede ya na (default = True).
# # tabsize       # andze har Tab che ghadr bashe (default = 8)
#
# w = TextWrapper(expand_tabs=False, tabsize=3)
#
# print(w.fill(s))