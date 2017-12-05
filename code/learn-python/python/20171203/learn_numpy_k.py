import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([10, 10, 10])
c = np.tile(b, (4, 1))
d = a + c
print(a)
print(b)
print(c)
print(d)
# 用广播机制：
#c = a + b
