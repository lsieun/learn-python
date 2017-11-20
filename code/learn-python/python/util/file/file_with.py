#异常处理的简单写法
path = "D://mynote.txt"
with open(path,"r",encoding="utf-8") as f:
    for line in f.readlines():
        print(line)