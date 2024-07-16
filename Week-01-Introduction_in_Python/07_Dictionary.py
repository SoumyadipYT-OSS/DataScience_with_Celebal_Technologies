student = {'name': 'Soumyadip', 'age': 21, 'courses': ['Math', 'DataScience']}

print(student)

print(student['courses'])

print(student.get('phone', 'Not Found'))    # Returns 'Not Found' if the key is not found

student['phone'] = '555-5555'
student['product'] = 'HP Laptop'

print(student.get('phone', 'Not Found'))

student.update({'name': 'Subhasish', 'age': 22, 'phone': '555-5555', 'product': 'Asus Laptop'})
print(student)

del student['product']
print(student)

age = student.pop('age')
print(student)
print(age)  # still age prints because it is stored in the variable 'age'
# though 'age' is deleted from the dictionary, it is stored in the variable 'age'


print(len(student))
print(student.keys())
print(student.values())
print(student.items())
