#coding=utf-8

from socket import *
from time import ctime
import threading


host = "192.168.1.154"
port = 8880
BUFSIZE = 1024
ADDR = (host,port)

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind(ADDR)
sockfd.listen(5)
def fun1(connfd,addr):
    print "线程已开启连接：",addr

    while True:
        data = connfd.recv(BUFSIZE)
        if data == "\r\n":
            break
        print data
        connfd.send("这是从服务器返回过来的！时间%s+++++:%s"%(ctime(),data))

if __name__ == "__main__":
    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt as e:
            print e

        t = threading.Thread(target = fun1,args = (connfd,addr))
        t.setDaemon(1)
        t.start()

    t.join()


sockfd.close()
connfd.close()
