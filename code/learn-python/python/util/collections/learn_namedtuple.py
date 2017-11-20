#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#namedtuple
#namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便


#普通tuple
tuple = ("A","B","C")
print(tuple[0]) #通过角标值来获取数据

#namedtuple，如果作为一个单独的数据结构，就是每个元素都有名称，并且一旦创建，无法修改
from collections import namedtuple
Point = namedtuple("Point",["name","age","sex"])
p = Point("旺财","3","male")
print(p.name)



