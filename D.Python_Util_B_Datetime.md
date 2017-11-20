# Python常用代码：datetime #

1. 获取当前时间
2. 对时间进行加减
3. 将date类型转换成特定格式的字符串
4. 将字符串解析成Date类型


## 1、获取当前时间 ##

	from datetime import datetime
	#获取当前时间
	now = datetime.now()
	print(now)

输出

	2017-11-20 22:49:17.867204

## 2、对时间进行加减操作 ##

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

输出：

	2017-11-20 22:54:54.355204
	2017-11-23 00:54:54.355204
	2017-11-20 00:54:54.355204


## 3、对时间进行格式化输出 ##

	from datetime import datetime
	
	#将date转换为字符串
	now = datetime.now()
	print(now)
	str_time = now.strftime("%Y-%m-%d %H:%M:%S")
	print(str_time)

输出：

	2017-11-20 22:52:04.861204
	2017-11-20 22:52:04

## 4、由字符串解析为时间 ##

	from datetime import datetime
	#将字符串转为date类型
	date = datetime.strptime("2017-11-19 22:08:29","%Y-%m-%d %H:%M:%S")
	print(date)

输出：

	2017-11-19 22:08:29


>至此结束







