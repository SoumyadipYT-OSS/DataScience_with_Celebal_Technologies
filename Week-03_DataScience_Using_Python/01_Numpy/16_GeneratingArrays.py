import numpy as np

# some machine learning approaches

print("generate 0 floating value array or a matrix")
a = np.zeros((2,3)) # 2 columns and 3 rows
print(a, " ", a.dtype)

print("generate 1 floating value array or a matrix")
a = np.ones((2,3))
print(a, " ", a.dtype)

print("generate the 5.0 float value matrix")
a = np.full((2,3), 5.0)
print(a, " ", a.dtype)

print("generate identity matrix of 3x3")
a = np.eye(3)
print(a, " ", a.dtype)

print("generate an array 1x1 from 0 to 19 int64 type")
a = np.arange(20)
print(a, " ", a.dtype)

print()
a = np.linspace(0,10,5)
print(a)
