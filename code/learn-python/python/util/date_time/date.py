from datetime import datetime, timedelta

#将date转换为字符串

#获取当前时间
now = datetime.now()
print(now)
str_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(str_time)


#将字符串转为date类型
date = datetime.strptime("2017-11-19 22:08:29","%Y-%m-%d %H:%M:%S")
print(date)

#对日期进行修改：时间加减
now = datetime.now()
#加2小时
now += timedelta(hours=2)
#加2天
now += timedelta(days=2)
print(now)
#减3天
now += timedelta(days=-3)
print(now)


