#coding=utf-8

from socket import *
import sys


host = sys.argv[1]
port = int(sys.argv[2])
bufsize = 1024
ADDR = (host,port)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(ADDR)

while True:
    data = raw_input("请输入消息：>>>")
    if data == "\r\n":
        break
    sockfd.send(data)

    data = sockfd.recv(bufsize)
    if data == "\r\n":
        break
    print data

sockfd.close()
