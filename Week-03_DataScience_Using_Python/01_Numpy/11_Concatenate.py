import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

# hstack,vstack
c = np.hstack((a,b))
print(c)

d = np.vstack((a,b))
print(d)
