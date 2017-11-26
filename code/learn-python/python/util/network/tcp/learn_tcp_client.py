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