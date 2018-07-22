# Python常用代码：文件操作 #

Python的常用操作有：文件操作、日期类、集合、Urllib、网络通信。

## 1、文件操作 ##
文件操作模式：

1. 读文件
2. 写文件（覆盖、追加）

文件操作的三种方式

	r = read 读取文件
	w = write 写入文件 覆盖掉原来的内容
	a = append 追加写入，不会覆盖原来的内容

### 1.1、读取全部 ###

	#读文件（读取全部内容）
	path = "D://mynote.txt"
	f = open(path,"r",encoding="utf-8")
	data = f.read()
	print(data)
	f.close()

### 1.2、一行一行读取 ###

	#读文件（一行一行读取）
	path = "D://mynote.txt"
	f = open(path,"r",encoding="utf-8")
	for line in f.readlines():
	    print("----->" + line)
	f.close()

### 1.3、覆盖写入 ###

	#写文件（覆盖写）
	path = "D://mynote.txt"
	f = open(path,"w",encoding="utf-8")
	f.write("我爱Python")
	f.close()

### 1.4、追加写入 ###

	#写文件（追加写）
	path = "D://mynote.txt"
	f = open(path,"a",encoding="utf-8")
	f.write("\r\n")
	f.write("Python爱我")
	f.close()

### 1.5、异常处理的两种方式 ###

第一种方式try...finally：

	try:
	    path = "D://mynote.txt"
	    f = open(path,"r",encoding="utf-8")
	    for line in f.readlines():
	        print("-->" + line)
	finally:
	    f.close()

第二种方式with：

	#异常处理的简单写法
	path = "D://mynote.txt"
	with open(path,"r",encoding="utf-8") as f:
	    for line in f.readlines():
	        print(line)






