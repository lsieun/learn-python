#使用list存储数据时，按索引访问元素很快
#但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除的效率很低
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a','b','c','d'])
q.append("e")      #添加元素
q.appendleft("0")
print(q)
left = q.popleft() #删除元素
print(left)
print(q)
right = q.pop()
print(right)
print(q)