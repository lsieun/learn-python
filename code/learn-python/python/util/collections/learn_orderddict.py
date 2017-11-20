#OrderedDict
#OrderedDict的Key会按照插入的顺序排列，不是key本身排序
from collections import OrderedDict
d = OrderedDict([('a',1),('b',3),('c',2)])
for i in d.items():
    print(type(i))
    print(i)
    print(i[1])
    print("----------")