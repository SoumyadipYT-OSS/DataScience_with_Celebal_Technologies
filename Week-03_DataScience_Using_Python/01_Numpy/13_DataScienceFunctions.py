import numpy as np

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)
print(a.sum(axis=1))
print(a.mean(axis=None))
print(a.var(axis=None))
print(a.std(axis=None))
print(np.std(a, axis=None))
print(np.max(a, axis=None))
