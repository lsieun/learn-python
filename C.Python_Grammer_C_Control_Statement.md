# Python基础:控制语句 #

## 1、if语句 ##

	if <条件判断1>:
	    <执行1>
	elif <条件判断2>:
	    <执行2>
	elif <条件判断3>:
	    <执行3>
	else:
	    <执行4>

## 2、for循环 ##

Python中常用的结构有list/dict/set/tuple，它们都可以使用for循环。

list

	#list = [1,2,3,4,5,6]
	list = range(100)
	for item in list:
	    print(item)

map

	map = {"a":"A","b":"B","c":"C"}
	for item in map:
	    print(item)
	
	for item in map.items():
	    print(item)
	
	for key in map.keys():
	    print(key)
	
	for value in map.values():
	    print(value)

set

	set = set(["A","B","C","D"])
	for item in set:
	    print(item)
	
tuple

	t = ("a","b",1,2,[3,4,5])
	for item in t:
	    print(item)


## 3、while循环 ##

	n = 0
	while n <= 10:
	    print(n)
	    n += 1

## 4、while和for循环语句中的continue和break关键字 ##

while中的break

	n = 0
	while True:
	    n += 1
	    if n == 7:
	        break
	    print(n)

while中的continue

	n = 0
	while n < 10:
	    n += 1
	    if n == 7:
	        continue
	    print(n)




> 至此结束











