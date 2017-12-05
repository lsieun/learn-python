import numpy as np
a = np.arange (4)
b = a
c = a
d = b

a[0]=10  #a = ? b = ? c= ? d = ?
# print(a)
# print(b)
# print(c)
# print(d)
b = a.copy()
a [0] = 9
#b = ?
print(a)
print(b)
print(c)
print(d)