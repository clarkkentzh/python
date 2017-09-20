#!/usr/bin/python
#coding=utf-8

from SocketServer import *
import socket,os

class Servers(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print ("已建立连接：",addr)
        while True:
            data = self.request.recv(1024)
            if data == "\r\n":
                break
            print (data)
            self.request.send("从服务器返回的数据：%s"%data)

server = Servers(("192.168.1.154",8880),Handler)
server.serve_forever()
