import numpy as np

#第一種方法
list1 = [1,2,3]
list2 = [[1,2,3],[4,5,6]]

a = np.array(list2)
print(type(a))

print(a.ndim)#秩
print(a.shape)#每個維度的長度
print(a.size)#數組的所有元素的個數
print(a.dtype)
#a.dtype = np.float32
print(a)
a.shape=(3,2)
print(a)


