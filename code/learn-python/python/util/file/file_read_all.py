#读文件（读取全部内容）
path = "D://mynote.txt"
f = open(path,"r",encoding="utf-8")
data = f.read()
print(data)
f.close()