#读文件（一行一行读取）
path = "D://mynote.txt"
f = open(path,"r",encoding="utf-8")
for line in f.readlines():
    print("----->" + line)
f.close()