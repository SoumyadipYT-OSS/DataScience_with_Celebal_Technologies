myTuple = ("Pomegranate", "Banana", "Apple")
myit = iter(myTuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("\n")

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("\n")


# Looping Through an Iterator
fruit_tuple = ("mango", "apple", "pomegranate")
for i in fruit_tuple:
    print(i)
