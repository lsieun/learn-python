
#str转换成byte数组的两种方式
#（1）直接通过str.encode(encoding="utf-8")
#（2）通过bytes("字符串",encoding="utf-8")得到比特数组

#将bytes转换成字符串的两种方式
#（1）通过对象自带的decode()方法进行解码 ，例如：data.decode("utf-8")
#（2）创建一个str对象，例如：str(data,encoding="utf-8")

originStr = "I love 游泳"
mybyte01 = bytes(originStr,encoding="utf-8")
mystr01 = str(mybyte01,encoding="utf-8")
mybyte02 = originStr.encode(encoding="utf-8")
mystr02 = mybyte02.decode(encoding="utf-8")
print(originStr)
print(mybyte01)
print(mybyte02)
print(mystr01)
print(mystr02)
