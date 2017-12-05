#coding:utf-8
import numpy as np
a = np.arange(9).reshape((3,3))
print(a)
print(a.sum())
print(a.sum(1)) #1代表行相加的和，0表示列相加的和

#使用切片，求某一行的和。
#為什麽要使用切片呢？在使用矩陣過程中，可能只計算有價值的數據
print(a[0].sum())
