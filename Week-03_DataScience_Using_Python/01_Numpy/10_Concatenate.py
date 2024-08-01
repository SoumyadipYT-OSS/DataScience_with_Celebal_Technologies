import numpy as np

print("Example 1")
a = np.array([[1,2], [3,4]])
print(a)
print("\nExample 2")
b = np.array([[5,6]])
print(b)
#----------------------------
print("\nExample 3")
c = np.concatenate((a,b), axis=None)
print(c)
print("\nTranspose")
d = np.concatenate((a,b.T), axis=1) # b.T makes the transpose
print(d)
