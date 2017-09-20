#coding=utf-8

from socket import *
from time import ctime


host = "192.168.1.154"
port = 8880
BUFSIZE = 1024
ADDR = (host,port)

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind(ADDR)
sockfd.listen(5)

while True:
    print "等待连接......"
    connfd,addr = sockfd.accept()
    print "已连接：",addr

    while True:
        data = connfd.recv(BUFSIZE)
        if data == "\r\n":
            break
        print data
        connfd.send("这是从服务器返回过来的数据！时间%s+++++:%s"%(ctime(),data))

sockfd.close()
connfd.close()
