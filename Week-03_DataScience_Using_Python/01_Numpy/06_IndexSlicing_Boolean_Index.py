import numpy as np

# boolean indexing and checking
a = np.array([[1,2], [3,4], [5,6]])
print("a: ", a)

bool_idx = a > 2
print("Checking each element value > 2: \n", bool_idx)
print("1D array as per logic: ", a[bool_idx]) # only print greater than 2 value from the array 'a'

