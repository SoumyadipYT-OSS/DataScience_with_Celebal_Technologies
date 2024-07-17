# In python, __init__() is a built-in function.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Soumyadip", 20)

print(p1.name)
print(p1.age)