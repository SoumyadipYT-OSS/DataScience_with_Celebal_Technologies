import numpy as np

x = np.array([1,2])
print(x)
print(x.dtype)

print("\n")

y = np.array([1.0, 2.0], dtype=np.int64)
print(y)
print(y, " ", y.dtype)

z = np.array([1.0, 2.0], dtype=np.int32)
print(z)
print(z, " ", z.dtype)
