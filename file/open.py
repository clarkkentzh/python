#coding=utf-8
import sys
fd = open("text.txt")
# print dir(fd)   # 打印文件描述符(也就是文件对象)的方法
#*****************************read********************************
s = fd.read()   #查全部
# s = fd.readline()  # 只查一行就返回
# s = fd.readlines()   #　把每一行都分开都放到一个列表内
# print s[1].decode("utf-8")   #　列表内元素的转码
print s

# 也可以用for循环打印全部内容
# for line in fd:
#     print line,

fd.close()
####**************************write********************************
# 权限为w+会每次都清空原先的数据,a+则是在原先的数据追加
fds = open("writ.txt","w+")

# 换行得自己手动加\n
fds.write("hahahahahahahahah \n zzzzz\n")
fds.write("zhaohong\n")

# writelines是将列表分解写入文件
l = ["haha","zzzzworld"]
fds.writelines(l)

fds.close()
#******************************************************************
# print sys.stdin.readline()    # 从标准输入的数据

# 需要人为的关闭，否则会占用系统资源,当然也可以用with生成fd就不用close了
# with open("text.txt","w+") as fd:
#     pass
