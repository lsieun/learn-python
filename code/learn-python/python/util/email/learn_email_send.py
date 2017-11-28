import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from_name = "zhangsan"
from_email = "zhangsan@lsieun.com"

to_name = "李四"
to_email = "lisi@lsieun.com"

title = "my first python 邮件"
content = "Hello World，你好,python"

smtp_addr = "192.168.80.128" #smtp.lsieun.com

user="zhangsan@lsieun.com"
passwd = "123456"

msg = MIMEText(content,'plain',"utf-8")
#msg是一个map
msg['Subject'] = Header(title)
msg['From'] = formataddr((from_name,from_email),charset="utf-8")
msg['To'] = formataddr((to_name,to_email),charset="utf-8")

#导入发送邮件的包
#创建服务
server = smtplib.SMTP(host=smtp_addr,port=25)
server.login(user=user,password=passwd)
server.sendmail(
    formataddr((from_name,from_email),charset="utf-8"),
    formataddr((to_name,to_email),charset="utf-8"),
    msg.as_string())
#发送完成后退出
server.quit()