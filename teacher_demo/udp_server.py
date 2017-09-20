#!/usr/bin/python

from socket import *
from time import ctime

HOST = '192.168.1.211'
PORT = 8888 
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM,0)
sockfd.bind(ADDR)

while True:
    print('waiting for message...')
    data,addr = sockfd.recvfrom(BUFSIZE)
    sockfd.sendto(('[%s] :%s'%(ctime(),data)).encode(),addr)
    
    print("recv from and send to ",addr)

sockfd.close()

