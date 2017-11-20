#读取文件的异常处理
#
try:
    path = "D://mynote.txt"
    f = open(path,"r",encoding="utf-8")
    for line in f.readlines():
        print("-->" + line)
finally:
    f.close()