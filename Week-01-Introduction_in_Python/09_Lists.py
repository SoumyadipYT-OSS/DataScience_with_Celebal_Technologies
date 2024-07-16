# Example 1
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(courses[0])  # List is like an array, so it starts from 0
print(courses[3])
print(courses[-1])  # Negative index starts from the end of the list
print(courses[-2])

# Slicing
print(courses[0:2])  # Prints the elements from index 0 to 1
print(courses[:2])  # Prints the elements from index 0 to 1

# 'append' method (adds to the end of the list)
courses.append('Art')  # Adds 'Art' to the end of the list
print(courses)
# 'insert' method (index, value)
courses.insert(0, 'Art')  # Adds 'Chemistry' at index 0
print(courses)
print(courses[2:])  # Prints the elements from index 2 to the end of the list
print(courses[:])  # Prints the entire list


# Example 2
courses_2 = ['Sport', 'Music']
print(courses_2)
courses_2.insert(1, 'Yoga')
print(courses_2)
courses_2.sort(reverse=True)  # Sorts the list in reverse order
print(courses_2)

sorted_courses = sorted(courses_2)  # Sorts the list in ascending order
print(sorted_courses)