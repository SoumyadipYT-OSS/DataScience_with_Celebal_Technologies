'''

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

'''


# Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
beautiful_person = Person("Antara", "Biswas")
beautiful_person.printname()


# Create a Child Class
class Actor(Person):
  pass  # Pass keyword when you do not want to add any other properties

class Actress_with_National_Award(Person):
  def award(self):
    print(self.firstname, self.lastname, "won National film award")
famous_actress = Actress_with_National_Award("Konkona", "Sen")
famous_actress.printname()
famous_actress.award()

#Anasuya Sengupta
class Actress_with_InternationalAward(Person):
  def __init__(her, fname, lname, grad, uni):
    super().__init__(fname, lname)  # super() function that will make the child class inherit all the methods and properties from its parent.
    her.graduated = grad
    her.university = uni
  
  def graduationYear(her):
    print("She graduated in", her.graduated)
  
  def graduationFrom(her):
    print("She graduated from", her.university)

  def internationalAward(her):
    print(her.firstname, her.lastname, "won the internatioanl film award")

print("\n")

starPerson = Actress_with_InternationalAward("Anasuya", "Sengupta", 1995, "Delhi University")
starPerson.printname()
starPerson.graduationYear()
starPerson.graduationFrom()
starPerson.internationalAward()
