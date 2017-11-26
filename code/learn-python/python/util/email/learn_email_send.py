import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from_name = "9527"
from_email = "maoxiangyi@itcast.cn"

to_name = "zhangsan"
to_email = "maoxiangyi@itcast.cn"

title = "abc"
content = "Hello World"


smtp_addr = "smtp.itcast.cn"

user="maoxiangyi@itcast.cn"
passwd = "123455"

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