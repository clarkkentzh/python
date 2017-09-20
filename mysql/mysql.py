#coding=utf-8

import MySQLdb
import getpass
# getpass类似raw_input，终端输入是隐藏的数据

user = raw_input("用户名：")
password = getpass.getpass("密码：")
# db是数据库对象,打开数据库
db = MySQLdb.connect("localhost",user,password,"zhao")


# 使用cursor()方法获取操作游标 ,也就是数据库操作对象
cursor = db.cursor()

# 执行一条sql语句
# cursor.execute("select version()")
cursor.execute("select * from stu")

# 游标活动状态
print cursor.description
# 配合execute得到sql语句执行的结果
# data = cursor.fetchall()
# data = cursor.fetchmany()
data = cursor.fetchone()


print data

cursor.close()
db.close()
