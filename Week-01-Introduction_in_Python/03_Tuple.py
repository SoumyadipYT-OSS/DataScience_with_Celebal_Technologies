tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# tup.sort()  # AttributeError: 'tuple' object has no attribute 'sort'
s_tup = sorted(tup) # Returns a list
print('Tuple Variable:\t', tup)
print('Sorted Variable:\t', s_tup)