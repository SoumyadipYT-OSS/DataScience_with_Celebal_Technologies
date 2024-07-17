# __str__() Function

print("WITHOUT the __str__() function:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Soumyadip", 20)
print("p1: ", p1)



print("\nWITH the __str__() function:")
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
p2 = Person2("Subhasis", 21)
print("p2: ", p2)
