import numpy as np

a = np.arange(1, 7)
print("A: \n", a)
print(a.shape)
b = a[:, np.newaxis]
print("\nB: \n", b)
c = a[np.newaxis, :]
print("\nC: \n", c)
