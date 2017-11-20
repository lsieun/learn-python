#写文件（追加写）
path = "D://mynote.txt"
f = open(path,"a",encoding="utf-8")
f.write("\r\n")
f.write("阿芬也爱我")
f.close()