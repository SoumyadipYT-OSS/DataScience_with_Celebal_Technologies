'''
    The self parameter is a reference to the current instance of the class,
    and is used to access variables that belongs to the class.

    It does not have to be named self , you can call it whatever you like,
    but it has to be the first parameter of any function in the class:

'''

class Person:
    def __init__(myobject, firstName, lastName):
        myobject.fN = firstName
        myobject.lN = lastName
    
    def myfunc(abc):
        print("Hi! my name is " + abc.fN + " " + abc.lN)

p1 = Person("Soumyadip", "Majumder")
p1.myfunc()

# modifying the object properties
p1.fN = "Babai"
# delete object properties
del p1.lN
print(p1.fN)  # p1.lN gives you an error
# Delete Objects using 'del' keyword
del p1
