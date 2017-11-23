"""
1、创建一个socket连接，得到一个client端
2、连接服务器
3、获取数据，并打印出来
"""
import socket

#1、创建一个socket_client对象
import time

socket_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
#2、连接服务器
socket_client.connect(("127.0.0.1",8888))
#3、获取服务端的数据，并打印
data = socket_client.recv(1024)
#4、处理解码的问题：返回的数据是byte数组，需要转换成字符串（两种方法）
print(data)
print(data.decode("utf-8"))
print(str(data,encoding="utf-8"))
#将bytes转换成字符串的两种方式
#（1）通过对象自带的decode()方法进行解码 ，例如：data.decode("utf-8")
#（2）创建一个str对象，例如：str(data,encoding="utf-8")


#发送数据到服务端
socket_client.send("我爱Python".encode(encoding="utf-8"))
socket_client.send("我爱阿芬".encode(encoding="utf-8"))

while True:
    data = socket_client.recv(1024).decode("utf-8")
    if data != "":
        print(data)
        time.sleep(1)
        socket_client.send("我爱阿芬".encode(encoding="utf-8"))