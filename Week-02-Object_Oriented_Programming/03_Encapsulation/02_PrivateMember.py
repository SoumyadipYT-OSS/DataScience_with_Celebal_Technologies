# In python, there is no existance of Private instance variables that cannot be accessed except inside a class.

# Note: Python's private and protected members can be accessed outside the class through 'python name mangling'


class Base:
    def __init__(self):
        self.a = "DataScience" # normal variable
        self._protectedVar = "AI"
        self.__privateVar = "MachineLearning"  # private variable using '__' sign


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__privateVar)


obj1 = Base()
print(obj1.a)
print(obj1._protectedVar)
# print(obj1.__privateVar)   this will give you an error, because it is private variable
# obj2 = Derived()   
'''
    obj2 = Derived()

    It will also gives you an error, because derived class inherits the 
    base class, so it will call the all variables even try to call the private 
    variable of the base class, so compiler throws an error
'''
