# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple is immutable, which means that we cannot change, add, or remove items after the tuple has been created.

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'  # This will throw an error as tuple is immutable