# Object can also contain methods. Methods in objects are functions that belong to the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Soumyadip Majumder", 21)
p1.myfunc()

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
