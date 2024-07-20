import numpy as np

a =  np.array([1, 2, 3])
print(a)
print(a.shape)  # returns dimension of the array in tuple with no of elements of each dimension
print(a.dtype)  # returns datatype of the array
print(a.ndim)   # dimension number
print(a.size)   # returns total number of elements
print(a.itemsize)  # returns byte-size of each element
print(a[0])
a[0] = 10
print(a)


# mathematical operations
b = a * np.array([2, 0, 2])
print(b)
