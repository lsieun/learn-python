#Counter
#Counter是一个简单的计数器，例如统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)


#使用dict进行实现
map = dict()
str = "hello"
for ch in str:
    value = map.get(ch)
    if value == None:
        map[ch] = 1
    else:
        map[ch] = value + 1
print(map)
