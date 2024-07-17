class Number_Sequence:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

my_class = Number_Sequence()
print(my_class)
myiter = iter(my_class)

print("\n")

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
