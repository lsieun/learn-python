#写文件（覆盖写）
path = "D://mynote.txt"
f = open(path,"w",encoding="utf-8")
f.write("我爱阿芬")
f.close()