list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)
# Both list_1 and list_2 are pointing to the same memory address.
# Any change in one list will affect the other list as well.

# getting the memory address of the list
print(hex(id(list_1)))
print(hex(id(list_2)))

list_2 = list_1[:] # This will create a new list with the same elements as list_1
# Now list_1 and list_2 are pointing to different memory addresses.
print(list_1)

# getting the NEW memory address of the list
print(hex(id(list_1)))
print(hex(id(list_2)))  # This will be different from the previous memory address