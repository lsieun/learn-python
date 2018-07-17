# TCP #

## TCP服务器 ##

tcp服务器流程如下：

（1）socket创建一个套接字
（2）bind绑定ip和port
（3）listen使套接字变为可以被动连接
（4）accept等待客户端的链接
（5）recv/send接收发送数据

```python
from socket import *

serverSocket = socket(AF_INET,SOCK_STREAM)

#绑定地址
serverAddr = ('',8899)
serverSocket.bind(serverAddr)

#listening
serverSocket.listen(5)

#接收客户端连接
clientSocket, clientAddr = serverSocket.accept()

#与客户端通信
recvData = clientSocket.recv(1024)
print(recvData)

clientSocket.send(b"World")

#关闭Socket
clientSocket.close()
serverSocket.close()

```

## TCP客户端 ##

```python
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

#连接服务器
serverAddr = ('192.168.80.15',8899)
clientSocket.connect(serverAddr)

#发送数据
clientSocket.send(b"hello")

#接收数据
recvData = clientSocket.recv(1024)
print(recvData)

clientSocket.close()

```


