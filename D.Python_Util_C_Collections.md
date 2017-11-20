# Python常用代码：collections增强 #



## namedtuple ##

tuple一旦被创建无法修改，获取tuple中的数据，只能通过角标值`t[index]`进行获取；但是，要记住角标值与值之间的关系有些麻烦。

namedtuple是基于tuple的扩展，能够给tuple中的每个元素起个名字。

示例：普通tuple通过元素的角标值来获取数据

	#普通tuple
	tuple = ("A","B","C")
	print(tuple[0]) #通过角标值来获取数据

示例：namedtuple通过元素的名称来获取数据

	#namedtuple，如果作为一个单独的数据结构，就是每个元素都有名称，并且一旦创建，无法修改
	from collections import namedtuple
	Point = namedtuple("Point",["name","age","sex"])
	p = Point("旺财","3","male")
	print(p.name)

## deque ##

相当于Java中的LinkedList。特性：查询慢，删除和修改快。

示例：

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

输出：

	deque(['0', 'a', 'b', 'c', 'd', 'e'])
	0
	deque(['a', 'b', 'c', 'd', 'e'])
	e
	deque(['a', 'b', 'c', 'd'])


## OrderdDict ##

可以排序的字典，按照插入顺序排序

示例：

	from collections import OrderedDict
	d = OrderedDict([('a',1),('b',3),('c',2)])
	for i in d.items():
	    print(type(i))
	    print(i)
	    print(i[1])
	    print("----------")

输出：

	<class 'tuple'>
	('a', 1)
	1
	----------
	<class 'tuple'>
	('b', 3)
	3
	----------
	<class 'tuple'>
	('c', 2)
	2
	----------

## Counter ##

Counter是一个简单的内置计数器，例如统计字符出现的个数

示例：

	from collections import Counter
	c = Counter()
	for ch in 'programming':
	    c[ch] = c[ch] + 1
	    
	print(c)

输出：


	Counter({'m': 2, 'r': 2, 'g': 2, 'a': 1, 'i': 1, 'n': 1, 'p': 1, 'o': 1})


使用dict实现如下：

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

输出：

	{'l': 2, 'o': 1, 'e': 1, 'h': 1}

>至此结束


















