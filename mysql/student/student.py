#coding=utf-8

import MySQLdb
import getpass,sys

db = MySQLdb.connect("localhost","root","123456","zhao")
cur = db.cursor()

def stu():
    print "\n"
    print "*************     学生管理系统(管理员)     *************"
    print "***  1.insert  2.delete  3.update  4.show  5.return  ***"
    print "********************************************************"
    print "\n"

    ins = raw_input("请输入指令：")
    if ins == "1":
        name = raw_input("请输入数据name:")
        age = int(raw_input("请输入数据age:"))
        score = float(raw_input("请输入数据score:"))
        try:
            cur.execute("insert into stus (name,age,score) values('%s',%d,%f)"%(name,age,score))
            db.commit()
        except:
            db.rollback()
        stu()
    elif ins == "2":
        ids = int(raw_input("请输入删除id:"))
        try:
            cur.execute("delete from stus where ids = %d"%ids)
            db.commit()
        except:
            db.rollback()
        stu()
    elif ins == "3":
        ids = int(raw_input("请输入ids:"))
        datas = raw_input("请输入更新字段名：")
        if datas == "name":
            zhi = raw_input("请输入值：")
            try:
                cur.execute("update stus set name='%s' where ids =%d"%(zhi,ids))
                db.commit()
            except Exception as e:
                db.rollback()
            stu()
        elif datas == "age":
            zhi = int(raw_input("请输入值："))
            try:
                cur.execute("update stus set age=%d where ids = %d"%(zhi,ids))
                db.commit()
            except:
                db.rollback()
            stu()
        elif datas == "score":
            zhi = float(raw_input("请输入值："))
            try:
                cur.execute("update stus set score=%f where ids = %d"%(zhi,ids))
                db.commit()
            except:
                db.rollback()
            stu()
    elif ins == "4":
        try:
            cur.execute("select * from stus")
            result = cur.fetchall()
            if result != ():
                print "%s    %s    %s    %s"%(cur.description[0][0],cur.description[1][0],cur.description[2][0],cur.description[3][0])
                for row in result:
                    ip = row[0]
                    name = row[1]
                    age = row[2]
                    score = row[3]
                    print " %d     %s   %d     %.1f\n"%(ip,name,age,score)
            else:
                print "\n"
                print "数据库信息为空！\n"
        except Exception as e:
            print e
            print "error no datas"

        stu()
    elif ins == "5":
        user()
def stu1():
    print "\n"
    print "***学生管理系统(用户)***"
    print "*** 1.show  2.return ***"
    print "************************"
    print "\n"
    ins = raw_input("请输入指令：")
    if ins == "1":
        try:
            cur.execute("select * from stus")
            result = cur.fetchall()
            if result != ():
                for row in result:
                    ip = row[0]
                    name = row[1]
                    age = row[2]
                    score = row[3]
                    print "id = %d , name = %s , age = %d , score = %.1f\n"%(ip,name,age,score)
            else:
                print "\n"
                print "数据库信息为空！\n"
        except Exception as e:
            print e
        stu1()
    elif ins == "2":
        user()

def user():
    print "\n"
    print "*********     登录注册     ********"
    print "*** 1.login  2.register  3.quit ***"
    print "***********************************"
    print "\n"
    ins = raw_input("请输入指令:")
    if ins == "1":
        name = raw_input("请输入账号：")
        password = getpass.getpass("请输入密码：")
        cur.execute("select * from user where name = '%s'"%name)
        data = cur.fetchone()
        if password == data[2]:
            if data[3] == 1:
                stu()
            else:
                stu1()
        else:
            print data
            print "密码输入错误！"
            user()
    elif ins == "2":
        name = raw_input("请设置账号：")
        password = getpass.getpass("请设置密码：")
        flog = int(raw_input("请选择权限(1或0)："))
        try:
            cur.execute("insert into user (name,pa,flog) values('%s','%s','%d')"%(name,password,flog))
            db.commit()
        except:
            db.rollback()
        user()
    elif ins == "3":
        sys.exit(0)

user()
db.close()
