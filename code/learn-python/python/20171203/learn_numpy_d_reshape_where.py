#coding:utf-8
import numpy as np

# list1 = [1,2,3,4]
# a = np.array(list1)
# print(a**2)

a = np.random.randint(0,10,(3,2))
b = np.arange(6).reshape((2,3))

#計算兩個矩陣相乘
c = a.dot(b)
#print(c)

#矩陣軒置計算
#print(a.T)

#生成一個隨機的bool矩陣 3x3
m = np.random.randn(9).reshape((3,3))
print(m)
bool_m = np.where(c>0,True,False)
print(bool_m)

#
c1 = np.random.randn(9).reshape((3,3))
c2 = np.random.randn(9).reshape((3,3))

f1 = np.where(c1>0,True,False)
f2 = np.where(c2>0,True,False)

#根據f1和f2的值來獲取一個新矩陣，規則 f1 & f2 都為true,取值0,f1為true，取值為1
print(np.where(f1 & f2),0,np.where(f1,1,np.where(f2,2,3)))

print(np.sqrt(4))

c3 = np.random.randn(2)
print(c3)
print(np.sum(c3))
print(c3.sum())
#求矩陣中大于0的值的和
print((c3>0).sum())




