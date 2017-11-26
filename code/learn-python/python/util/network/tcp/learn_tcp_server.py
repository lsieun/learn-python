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