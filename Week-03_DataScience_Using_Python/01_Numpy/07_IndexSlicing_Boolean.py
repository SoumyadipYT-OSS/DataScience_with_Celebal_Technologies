import numpy as np

print("\nExample 1")
a = np.array([
    [1, 2], [3, 4], [5, 6]
])
print(a)
print(a[a > 2])
b = np.where(a > 2, a, -1)

#---------------------------

print("\n Example 2")
a = np.array([10, 19, 30,41, 50, 61])
print(a)
even = np.argwhere(a%2==0).flatten()
print(a[even])
