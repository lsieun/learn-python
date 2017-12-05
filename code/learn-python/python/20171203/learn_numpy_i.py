import numpy as np
#增加维度
# a = np.arange(5)
# print(a)
# print(a[:, np.newaxis])
# print(a[np.newaxis, :])
#print(np.tile([1,2], 2))

#合并
# a = np.arange(10).reshape(2,5)
# print(a)
# print(a.ravel())
# print(a.resize(5,2))
b = np.arange(6).reshape(2,3)
# print(b)
c = np.ones((2,3))
# print(c)
d = np.hstack((b,c))              # hstack：horizontal stack 左右合并
#print(d)
#print("--"*20)
e = np.vstack((b,c))              # vstack: vertical stack 上下合并
# print(e)
f = np.column_stack((b,c))
# print(f)
g = np.row_stack((b,c))
#print(g)
#print("--"*20)
h = np.stack((b, c), axis=1)      # 按行合并
#print(h)
i = np.stack((b,c), axis=0)       # 按列合并
print(i)
print("--"*20)
# j = np.concatenate ((b, c, c, b), axis=0)   #多个合并

#分割
k = np.hsplit(i, 2)
l = np.vsplit(i, 2)
# m = np.split(i, 2, axis=0)
# n = np.split(i, 2,axis=1)
#
# o = np.array_split(np.arange(10),3)   #不等量分割
print(k)
print("--"*20)
print(l)


