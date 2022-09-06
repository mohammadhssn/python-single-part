"""
    python-method-chaining:
        Method chaining in Python is a technique in which you can call the methods of a class one after the other.
         Some Python libraries, such as pandas, NumPy, and Pillow, use this method to increase code readability.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def capitalize(self):
        self.name = self.name.capitalize()
        return self  # need for method-chaining

    @property
    def lower(self):
        self.name = self.name.lower()
        return self  # need for method-chaining

    def show(self):
        print(self.name)


person = Person('mohammadhssn')
person.lower.capitalize().show()  # Mohammadhssn
# (person == self) first -> person =  person.lower() --- second ->  person.capitalize() --- final -> person.show()
