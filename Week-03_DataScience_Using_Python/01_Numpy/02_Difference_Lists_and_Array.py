'''

    Difference between Lists and Array in python.

'''

import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])
print(l)    # list
print(a)    # array

l.append(4)
print("updated list: ", l)
new_values = [4, 5, 6]
new_array = np.append(a, new_values)
print("updated array: ", a)

# mathematical operation in numpy
a = a + np.array([4])   # this is broadcasting method
print("updated array with each element + 4: ", a)

