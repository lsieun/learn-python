from datetime import datetime
#将字符串转为date类型
date = datetime.strptime("2017-11-19 22:08:29","%Y-%m-%d %H:%M:%S")
print(date)