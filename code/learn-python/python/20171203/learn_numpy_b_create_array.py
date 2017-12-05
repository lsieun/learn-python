#第二種方法創建數組，使用arrange函數、random函數
import numpy as np
#b = np.arange(0,9)
#b = np.arange(9).reshape((3,3))
#b = np.arange(8).reshape((2,2,2))
#b = np.arange(16).reshape((2,2,2,2))
#b = np.random.randint(0,100)
b = np.random.randint(0,100,(4,3))
print(type(b))
print(b)

#arange([start,] stop[, step,], dtype=None)
#Return evenly spaced values within a given interval.

#randint(low, high=None, size=None, dtype='l')
#        Values are generated within the half-open interval ``[start, stop)``
#        (in other words, the interval including `start` but excluding `stop`).




