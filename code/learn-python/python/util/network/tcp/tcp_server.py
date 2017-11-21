"""
1. 创建socket.socket()
2. 绑定IP地址和端口号
3. 监听客户端的请求
4. 接收客户端的请求，并为之开辟一个线程来处理它的业务逻辑
"""
import socket
import threading

def run(sock,addr):
    print(addr)
    sock.send("Hello World")

#网络通信的基本知识
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
