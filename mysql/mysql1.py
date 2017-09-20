#coding=utf-8

import MySQLdb
import getpass

user = raw_input("用户名：")
password = getpass.getpass("密码：")

db = MySQLdb.connect("localhost",user,password,"zhao")
cursor = db.cursor()

# 如果有这个表，删除
cursor.execute("drop table if exits zh")

tab = """create table zh (
    id int(10) not null primary key auto_increment,
    name char(20) not null,
    age int,
    score int default 0
)"""

# 事务的一致性，操作完如果失败必须回退到之前状态
try:
    cursor.execute(tab)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
