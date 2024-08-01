import numpy as np

a = np.arange(1, 7)
print("A: \n", a)
print(a.shape)
b = a.reshape((3, 2))   # 3 columns and 2 rows
print("\nB: \n", b)
