#coding=utf-8

from socket import *
import sys,os


host = sys.argv[1]
port = int(sys.argv[2])
bufsize = 1024
ADDR = (host,port)


sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(ADDR)

ss = "\n******请输入以下参数******\n***********list***********\n*******get filename*******\n*******post filename******\n"
while True:
    data = raw_input("请输入消息：>>>")
    data1 = data.split(" ")
    if data1[0] == "\r\n":
        break
    elif data1[0] == "list":
        sockfd.send(data)
        while True:
            data = sockfd.recv(1024)
            if data == "ha":
                break
            print("%s"%data)
        print ss
    elif data1[0] == "get":
        sockfd.send(data)
        fd = open(data1[1],'wb')
        while True:
            data = sockfd.recv(1024)
            if data == "ha":
                break
            fd.write(data)
            fd.flush()
        print("get %s OK!"%data1[1])
        fd.close()
        print ss
    elif data1[0] == "post":
        sockfd.send(data)
        fd = open(data1[1],'rb')
        while True:
            data = fd.readline()
            if not data:
                sockfd.send("ha")
                break
            sockfd.send(data)
            sleep(0.1)
        print("put %s OK!"%data1[1])
        fd.close()
        print ss
    elif data1[0] == "ls":
        os.system("ls")
        print ss
    else:
        print ss
sockfd.close()
