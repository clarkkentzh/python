#coding=utf-8
fd = open("text.txt","r+")

fd.read(12)
print fd.tell()     # 文件读到的当前位置
fd.read(12)
print fd.tell()


fd.seek(0,1)
fd.write("赵宏")
