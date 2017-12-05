#coding:utf-8
#open('pdts.txt','r')

# 新建一个文件，文件名为:test.txt
#f = open('test.txt', 'w')

# 关闭这个文件
#f.close()

# f = open('d:\TerraTerch.docx','rb')
# data = f.read(1024)
# i = 0
# while data:
#     i += 1
#     print(i)
#     data = f.read(1024)
#
# print("over")
# f.close()

f = open('d:\TerraTerch.docx','rb')
newFile = open('d:\TerraTerch2.docx','wb')
data = f.read(1024)
i = 0
while data:
    i += 1
    print(i)
    newFile.write(data)
    data = f.read(1024)

print("over")
newFile.close()
f.close()