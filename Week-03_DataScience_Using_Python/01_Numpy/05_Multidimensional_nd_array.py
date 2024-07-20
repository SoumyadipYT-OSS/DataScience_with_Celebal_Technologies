import numpy as np

a = np.array([[1, 2, 6], [3, 4, 8]])
print(a)
print(a.shape)  # It will no of rows and columns in a tuple

print(a[0,0])   # value of 0th row and 0th column
print(a[0,2])

print(a[:,0]) # selecting all elements of column 0th index
print(a[0,:]) # selecting all elements of row 0th index


# nd arrays
print("a.T -> \n", a.T) # Transpose of a matrix


# np.linalg
a = np.array([[1,2], [3,4]])
print("np.linalg.inv: ", np.linalg.inv(a))
print("np.linalg.det: ", np.linalg.det(a))
c = np.diag(a)
print(np.diag(c))
