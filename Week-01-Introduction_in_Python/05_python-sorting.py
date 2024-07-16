class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


def e_sort_name(emp):    # Sorts the list based on the name
    return emp.name
def e_sort_age(emp):
    return emp.age
def e_sort_salary(emp):
    return emp.salary


s_employees1 = sorted(employees, key=e_sort_name)
s_employees2 = sorted(employees, key=e_sort_age)
s_employees3 = sorted(employees, key=e_sort_salary)

print(s_employees1)
print(s_employees2)
print(s_employees3)