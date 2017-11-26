"""
1、服务器的地址：pop.itcast.cn
2、账户、密码
3、创建连接poplib
4、登录
5、获取所有的邮件信息
6、解析其中的一个邮件
"""
import poplib
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr

server_info = "pop.itcast.cn"
user = "maoxiangyi@itcast.cn"
pwd = "123"

#1、创建邮件服务器的接收链接
client = poplib.POP3(host=server_info,port=110)
#2、登录服务器
client.user(user)
client.pass_(pwd)
#3、获取邮件信息
#3.1、通过list方法获取所有的邮件信息，得到本次请求可以获取多少个邮件
resp,list,octets = client.list()
print(resp)
print(list)
print(octets)
#3.2、获取某一封邮件的信息
# for i in range(len(list)):
#     i += 1
#     the_email = client.retr(i)
#     #print(the_email)
#     print(the_email[1])
the_mail = client.retr(len(list))[1]
print(the_mail)
#3.3、解析邮件（发件人《姓名和邮箱地址》、收件人《收件人和邮箱地址》、标题、内容
#字符串拼接都是+，也可以用join
the_mail_str = b'\r\n'.join(the_mail).decode(encoding="utf-8")
print(the_mail_str)
#工具类 Parser能够解析邮件，输入文件或数据
#坑：在将bytes转换成字符串时，要将每个元素用换行符分隔，否则没法解析
msg = Parser().parsestr(the_mail_str)
print(msg)
print(type(msg))
#3.3.1、获取发件人信息、收件人信息、标题、内容
print(msg.get("From"))
print(msg.get("To"))
print(msg.get("Subject"))
print(msg.get_payload())#内容

from_tuple = parseaddr(msg.get("From"))
print(from_tuple[0])#name
print(from_tuple[1])#email

to_info = parseaddr(msg.get("To"))
to_name = to_info[0]
print(to_info[1])
charset,value = decode_header(to_name)
print(value.encode(charset))

to_tupe = parseaddr(msg.get("To"))
print("name: " + to_name[0])
#如果收件人是中文，需要解析出来
#decode_header能否返回一个list，list中包含一个tuple，tuple中有两个元素(string,charset)
result = decode_header(to_tupe[0])[0]
#通过字符集将内容decode解码出来
name = result[0].decode('utf-8')
print(name)

#内容
#get_payload方法默认会对文章内容进行解析，即decode
#如果不需要默认解析，将decode置为True，就表示需要用户自己解析
print(msg.get_payload(decode=True).decode("utf-8"))