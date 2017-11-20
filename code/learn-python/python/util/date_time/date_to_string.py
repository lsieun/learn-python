from datetime import datetime

#将date转换为字符串
now = datetime.now()
print(now)
str_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(str_time)