
#文件操作的三种方式
#r = read 读取文件
#w = write 写入文件 覆盖掉原来的内容
#a = append 追加写入，不会覆盖原来的内容
#读文件（读取全部内容）
path = "D://mynote.txt"
f = open(path,"r",encoding="utf-8")
data = f.read()
print(data)
f.close()

#读文件（一行一行读取）
path = "D://mynote.txt"
f = open(path,"r",encoding="utf-8")
for line in f.readlines():
    print("----->" + line)
f.close()

#写文件（覆盖写）
path = "D://mynote.txt"
f = open(path,"w",encoding="utf-8")
f.write("我爱阿芬")
f.close()

#写文件（追加写）
path = "D://mynote.txt"
f = open(path,"a",encoding="utf-8")
f.write("\r\n")
f.write("阿芬也爱我")
f.close()