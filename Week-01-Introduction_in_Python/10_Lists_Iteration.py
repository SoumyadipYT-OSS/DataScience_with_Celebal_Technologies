# List is a collection which is ordered and changeable. Allows duplicate members.
# List is mutable, which means that we can change, add, and remove items in a list after it has been created.
courses = ['Geography', 'Math', 'Physics', 'CompSci']

print("\n Example of using 'for' loop: \n")
# Iterating through the list
for c in courses:
    print(c)

print("\n Example of using 'range' keyword: \n")
# Loop using 'enumerate' keyword
for index, course in enumerate(courses):
    print(index, course)

print("\n Example of using 'enumerate' keyword: \n")
# Using 'enumerate' keyword to start from a specific index
for index, course in enumerate(courses, start=1):
    print(index, course)


print("\n Example of using 'join' keyword: \n")
# Joining the list elements
course_str = ', '.join(courses)
print(course_str)


print("\n Example of using 'split' keyword: \n")
# Splitting the string into a new list variable
new_list = course_str.split(', ')
print(new_list)