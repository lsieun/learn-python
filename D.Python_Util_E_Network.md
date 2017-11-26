# Python常用代码：网络编程 #

Python网络编程有两种模式：TCP和UDP。TCP是可靠连接，能够保证数据不丢失；UDP不关心数据是否会丢失，在乎传输效率。

## 1、TCP编程 ##

1. 服务端
2. 客户端

客户端如何连接服务端，保证传输数据的可靠呢？

	三次握手

### 1.1、预备知识：线程和字符串编码 ###

在进行学习网络编程之前，需要了解一下**线程**和**字符串编码**的知识。

#### 1.1.1、线程 ####

创建线程的步骤：

	1、创建线程对象，指明线程运行的方法、线程名称 和 线程中运行方法所需要的参数
	2、启动线程

示例1：不带参数的线程

	import threading
	
	def run1():
	    print("我是一个线程。。。")
	
	#(1)创建一个线程，需要指定线程运行的方法，并且给一个名称
	thread1 = threading.Thread(target=run1,name="线程1")
	#(2)创建完线程之后,一定要启动
	thread1.start()

示例2：带参数的线程

	import threading
	
	
	def run2(param1,param2):
	    print("我是一个线程。。。" + param1)
	
	#创建一个线程，需要指定线程运行的方法，并且给一个名称
	#可以根据需求给定参数
	thread2 = threading.Thread(target=run2,name="线程2",args=("123","456"))
	thread2.start()

为了更清楚的理解，来看一下threading.Thread的构造器是如何定义的：

	class Thread:
	    """A class that represents a thread of control.
	
	    This class can be safely subclassed in a limited fashion. There are two ways
	    to specify the activity: by passing a callable object to the constructor, or
	    by overriding the run() method in a subclass.
	
	    """
	
	    def __init__(self, group=None, target=None, name=None,
	                 args=(), kwargs=None, *, daemon=None):
	        """This constructor should always be called with keyword arguments. Arguments are:
	
	        *group* should be None; reserved for future extension when a ThreadGroup
	        class is implemented.
	
	        *target* is the callable object to be invoked by the run()
	        method. Defaults to None, meaning nothing is called.
	
	        *name* is the thread name. By default, a unique name is constructed of
	        the form "Thread-N" where N is a small decimal number.
	
	        *args* is the argument tuple for the target invocation. Defaults to ().
	
	        *kwargs* is a dictionary of keyword arguments for the target
	        invocation. Defaults to {}.
	
	        If a subclass overrides the constructor, it must make sure to invoke
	        the base class constructor (Thread.__init__()) before doing anything
	        else to the thread.
	
	        """

#### 1.1.2、字符串编码 ####

其实，这包括两方面的内容：从str编码成byte数组 和 从byte数组解码为str

str转换成byte数组的两种方式

	（1）直接通过str.encode(encoding="utf-8")
	（2）通过bytes("字符串",encoding="utf-8")得到比特数组

将bytes转换成字符串的两种方式

	（1）通过对象自带的decode()方法进行解码 ，例如：data.decode("utf-8")
	（2）创建一个str对象，例如：str(data,encoding="utf-8")

示例：

	#str转换成byte数组的两种方式
	#（1）直接通过str.encode(encoding="utf-8")
	#（2）通过bytes("字符串",encoding="utf-8")得到比特数组
	
	#将bytes转换成字符串的两种方式
	#（1）通过对象自带的decode()方法进行解码 ，例如：data.decode("utf-8")
	#（2）创建一个str对象，例如：str(data,encoding="utf-8")
	
	originStr = "I love 游泳"
	mybyte01 = bytes(originStr,encoding="utf-8")
	mystr01 = str(mybyte01,encoding="utf-8")
	mybyte02 = originStr.encode(encoding="utf-8")
	mystr02 = mybyte02.decode(encoding="utf-8")
	print(originStr)
	print(mybyte01)
	print(mybyte02)
	print(mystr01)
	print(mystr02)

输出：

	I love 游泳
	b'I love \xe6\xb8\xb8\xe6\xb3\xb3'
	b'I love \xe6\xb8\xb8\xe6\xb3\xb3'
	I love 游泳
	I love 游泳

### 1.2、服务端编写 ###

	Java: ServerSoket(ip,port)
	Python: socket.socket()

服务器端编写的步骤：

1. 创建socket.socket()
2. 绑定IP地址和端口号
3. 监听客户端的请求
4. 接收客户端的请求，并为之开辟一个线程来处理它的业务逻辑

示例：

	import socket
	
	#创建服务
	socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM,proto=0)
	
	#绑定地址和IP
	socket_server.bind(("127.0.0.1",8888))
	
	#进入监听状态
	socket_server.listen()
	
	#接收客户端数据
	(sock,addr) = socket_server.accept()
	
	#处理接收的数据
	#打印IP地址 和 数据
	print(addr)
	data = sock.recv(1024)
	print(data)
	print(str(data,encoding="utf-8"))
	sock.send(bytes("我是Server",encoding="utf-8"))


### 1.3、客户端编写 ###

客户端编写步骤：

1、创建一个socket连接，得到一个client端
2、连接服务器
3、获取数据，并打印出来

示例:

	import socket
	
	#1、创建一个socket_client对象
	socket_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
	#2、连接服务器
	socket_client.connect(("127.0.0.1",8888))
	#3、与服务器交互
	#3.1、向服务器端发送数据
	socket_client.send("你是who?".encode(encoding="utf-8"))
	#3.2、获取服务端的数据，并打印
	data = socket_client.recv(1024)
	print(data.decode(encoding="utf-8"))

### 1.4、网络通信的基本知识 ###

socket类的构造器定义如下：

	class socket(_socket.socket):
	
	    """A subclass of _socket.socket adding the makefile() method."""
	
	    __slots__ = ["__weakref__", "_io_refs", "_closed"]
	
	    def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None):
	        # For user code address family and type values are IntEnum members, but
	        # for the underlying _socket.socket they're just integers. The
	        # constructor of _socket.socket converts the given argument to an
	        # integer automatically.
	        _socket.socket.__init__(self, family, type, proto, fileno)
	        self._io_refs = 0
	        self._closed = False

其中，包含的“网络通信的基本知识”如下：


	#family=AF_INET, type=SOCK_STREAM, proto=0
	
	#family是地址簇，也就是IP地址类型，常用的IP地址类型有两种：AF_INET和AF_INET6
	#AF = Address Family
	#INET = Internet
	#AF_INET = IPV4
	#AF_INET6 = IPV6
	
	#type
	#type表示数据传输的方式
	#type = SOCK_STREAM 面向连接传输方式，数据可以准确无误的到达另外一台机器，如果数据丢失就会重发，速度相对比较慢
	#type = SOCK_DGRAM 表示无连接的传输方式，不是安全可靠的，计算机只管传输数据，不做数据校验，相对较快。QQ使用的是这种方式。
	
	#proto:
	#传输协议：一般有TCP和UDP

### 1.5、多线程Socket示例 ###

知识点：多线程、socket网络通信基本知识

服务端：

	import socket
	import threading
	
	def run(sock,addr):
	    print(addr)
	    sock.send(bytes("Hello WorldAAA",encoding="utf-8"))
	    while True:
	        data = sock.recv(1024).decode("utf-8")
	        if data != "":
	            print(data)
	            sock.send((data + " 是的呢").encode("utf-8"))
	
	#创建服务
	socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM,proto=0)
	
	#绑定地址和IP
	#Bind the socket to a local address.  For IP sockets, the address is a pair (host, port);
	socket_server.bind(("127.0.0.1",8888))
	
	#进入监听状态
	socket_server.listen()
	
	while True:
	    #接收一个请求
	    #sock是网络通道，用来读写数据
	    #addr是客户端ip地址
	    (sock,addr) = socket_server.accept()
	    #创建线程
	    thread = threading.Thread(target=run,name="线程",args=(sock,addr))
	    #启动线程
	    thread.start()

客户端：

	import socket
	import time
	
	#1、创建一个socket_client对象
	socket_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
	#2、连接服务器
	socket_client.connect(("127.0.0.1",8888))
	#3、获取服务端的数据，并打印
	data = socket_client.recv(1024)
	#4、处理解码的问题：返回的数据是byte数组，需要转换成字符串（两种方法）
	print(data)
	print(data.decode("utf-8"))
	print(str(data,encoding="utf-8"))
	
	
	#发送数据到服务端
	socket_client.send("我爱Python".encode(encoding="utf-8"))
	socket_client.send("我爱阿芬".encode(encoding="utf-8"))
	
	while True:
	    data = socket_client.recv(1024).decode("utf-8")
	    if data != "":
	        print(data)
	        time.sleep(1)
	        socket_client.send("我爱阿芬".encode(encoding="utf-8"))
> 至此结束