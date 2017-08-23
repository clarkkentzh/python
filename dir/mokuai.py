#coding=utf-8

############################Python 标准库模块
import sys
# print sys.__doc__     #查看模块说明文档
# print dir(sys)        #显示模块包含属性列表
# print help(sys)       #查看模块的帮助文档
a = sys.argv
print a         #是变量，专门用来向Python解释器传递命令行参数
# sys.exit()       #这个方法用来推出当前程序
# print sys.path         #查找目录所在模块


import os
# os.rename("text.txt","os.txt")   #重命名一个文件
# os.remove()                      #删除一个文件
# os.system("ls")                  #执行系统命令


import time
# print time.localtime() #获取一个时间元组，记录当前时间
# print time.ctime()  #Mon Aug 21 10:28:56 2017   以时间戳为参数获取一个时间
# print time.time()  #获取从1970年1月1日0时0分0秒到现在的秒数

import random
# print random.random()   #得到（0，1] 之间的随机数
# print random.randint(1,5)  #[1,5]之间的随机整数
# print random.randrange(1,6,2)  #[1,6)之间的步长为2的随机整数
# print random.choice([1,2,3,4,5])  # 返回列表或元组中的一个随机数

import shutil

shutil.copyfile(file1,file2) # 复制文件，文件名加引号
shutil.copy(file1,dir1)   # 复制文件到文件夹
shutil.copytree(dir1,dir2)  # 复制文件夹
