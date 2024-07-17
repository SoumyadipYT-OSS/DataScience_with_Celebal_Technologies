# abs() | returns the absolute value of a number
num = -100
print(abs(num))  # Output: 100

# all() | returns True if all elements in the iterable are truthy (or if the iterable is empty)
numbers = [1, 2, 3, 4, 5]
print(all(numbers))  # Output: True

# any() | returns True if any element in the iterable is truthy
print(any(numbers))  # Output: True

# ascii() | returns a string containing ASCII characters
print(ascii('Hello, World!'))  # Output: 'Hello, World!'

# bin() | returns the binary string representation of an integer
num = 10
print(bin(num))  # Output: '0b1010'

# bool() | returns a boolean value from a given value
print(bool(1))  # Output: True

# bytearray() | returns a bytearray object
arr = bytearray([0x40, 0x41, 0x42])
print(arr)  # Output: bytearray(b'@AB')

# bytes() | returns a bytes object
print(bytes([0x40, 0x41, 0x42]))  # Output: b'@AB'

# callable() | returns True if the object is callable, False otherwise
def my_function():
    pass
print(callable(my_function))  # Output: True

# chr() | returns a string representation of a character
print(chr(65))  # Output: 'A'


# classmethod() | returns a class method object
class MyClass:
    def my_method(cls):
        return cls
obj = MyClass()
print(classmethod(obj.my_method))  # Output: <bound method MyClass.my_method of <class '__main__.MyClass'>>


# compile() | compiles a string or a source code object into a code object
code = compile('x = 5\ny = 10\nprint(x + y)', '', 'exec')
exec(code)  # Output: 15

# complex() | returns a complex number
print(complex(18, 4))

# delattr() | Deletes the specified attribute (property or method) from the specified object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John', 30)
delattr(person, 'age')
# print(person.age)  # Output: AttributeError: 'Person' object has no attribute 'age'


# dict() | creates a dictionary from a sequence of key-value pairs
pairs = [('a', 1), ('b', 2), ('c', 3)]
print(dict(pairs))  # Output: {'a': 1, 'b': 2, 'c': 3}


# dir() | returns a list of all attributes and methods of a given object
print("Here I have taken built-in List data structure or collection to see all methods")
print(dir(list))


# divmod() | returns both the quotient and remainder of a division
print(divmod(17, 3))  # Output: (6, 2)


# enumerate() | returns a tuple containing the index and value of each item in the iterable
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(f'{index}: {color}')

'''
    There are many more special methods are available in Python:
    Link is the below to check those methods:
    [ https://www.w3schools.com/python/python_ref_functions.asp ]
'''
