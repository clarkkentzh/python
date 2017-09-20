#!/usr/bin/python

from socket import *

HOST = '192.168.1.211'
PORT = 8888 
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM,0)

while True:
    data = input('>')
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,ADDR = sockfd.recvfrom(BUFSIZE)
    data = data.decode()

    if not data:
        break;
    print(data)

sockfd.close()

