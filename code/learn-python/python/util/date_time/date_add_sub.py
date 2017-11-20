from datetime import datetime, timedelta
#对日期进行修改：时间加减
now = datetime.now()
print(now)
#加2小时
now += timedelta(hours=2)
#加2天
now += timedelta(days=2)
print(now)
#减3天
now += timedelta(days=-3)
print(now)