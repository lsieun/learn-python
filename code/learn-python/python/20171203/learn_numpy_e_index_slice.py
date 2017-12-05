#coding:utf-8
import numpy as np
#多維數組的索引和切片

a = np.random.randint(0,10,(6,4))
print(a)

print(a[2][1])#通過索引取值：第三行第二列的值
print(a[2,1])
print(a[[2,1]])#取第3行和第2行

print(a[0]) #取第1行

print(a[0:3])#取第1行到第3行
print(a[:3])
print(a[[2,1]])#取第3行和第2行

#取第4行的第1列到第3列
print(a[3,:3])

#取后2行，前3列
#print(a[[-1,-3:-1],:3])


#第1、3、5行，后3列
print(a[[0,2,4],-3:])
#print(a[[0,2,4]][:,-3:])




