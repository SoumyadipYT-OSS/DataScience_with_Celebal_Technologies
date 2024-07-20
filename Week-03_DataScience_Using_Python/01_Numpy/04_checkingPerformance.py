# Performance between Python Lists and Numpy Array

# Important! : you cannot convert numpy array in list.

import numpy as np
from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

TIME = 1000    # 1000 milliseconds

def dot1():
    res = 0
    for i in range(len(A)):
        res += A[i] * B[i]
    return res

def dot2():
    return np.dot(a, b)


start = timer()
for t in range(TIME):
    dot1()
end = timer()
t1 = end - start


start = timer()
for t in range(TIME):
    dot2()
end = timer()
t2 = end - start

print('List calculation: ', t1)
print('np.dot', t2)
print('ratio', t1/t2)
