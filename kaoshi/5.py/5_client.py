#coding=utf-8
import MySQLdb
import getpass,sys
from socket import *

host = '192.168.1.154'
port = 8880
ADDR = (host,port)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(ADDR)

class Flog(Exception):
    pass

def user():
    print "\n"
    print "*********     登录注册     ********"
    print "*** 1.login  2.register  3.quit ***"
    print "***********************************"
    print "\n"
    ins = raw_input("请输入指令:")
    if ins == "1":
        while True:
            name = raw_input("请输入账号：")
            password = getpass.getpass("请输入密码：")
            data = "1 " + name + " " + password
            sockfd.send(data)
            datas = sockfd.recv(1024)
            if datas == "r":
                print "\n"
                print "+++++++++++++++++++++登录成功！"
                user()
            else:
                print "密码输入错误，请重新输入"
    elif ins == "2":
        while True:
            try:
                name = raw_input("请设置账号：")
                password = getpass.getpass("请设置密码：")
                flog = raw_input("请选择权限(1或0)：")
                print type(flog)
                if flog != "1" and flog != "0":
                    raise Flog("flog error!")
                data = "2 " + name + " " + password + " " + flog
                sockfd.send(data)
                datas = sockfd.recv(1024)
                if datas == "yes":
                    print "\n"
                    print "+++++++++++++++++++++注册成功！请登录！"
                    user()
                else:
                    print datas
            except Flog as e:
                print "\n"
                print e
                print "输入有误，请重新输入\n"

    elif ins == "3":
        sockfd.send("3")
        sys.exit(0)
    else:
        print "\n"
        print "您的输入有误！请重新输入！"
        sockfd.send("null")
        datas = sockfd.recv(1024)
        user()

user()
