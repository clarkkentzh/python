#!/usr/bin/python
#coding=utf-8

from SocketServer import *
import socket,os,sys
from time import sleep
class Servers(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print ("已建立连接：",addr)
        while True:
            data = self.request.recv(1024)
            data1 = data.split(" ")
            if data1[0] == "\r\n":
                break
            elif data1[0] == "list":
                files = os.listdir(".")
                if files == None:
                    break
                for filename in files:
                    if filename[0] != '.' and os.path.isfile(filename):
                        self.request.send(filename)
                    sleep(0.1)

                self.request.send("ha")
                print "list ok!"
            elif data1[0] == "get":
                try:
                    fd = open(data1[1],'rb')
                except:
                    self.request.send('FAIL')

                while True:
                    data = fd.readline()
                    if not data:
                        break
                    self.request.send(data)
                    sleep(0.1)
                fd.close()
                self.request.send("ha")
                print "get files success!"
            elif data1[0] == "post":
                try:
                    fd = open(data1[1],'wb')
                except:
                    self.request.send('FAIL')
                while True:
                    data = self.request.recv(1024)
                    if data == "ha":
                        break
                    fd.write(data)
                    fd.flush()
                fd.close()
                print "post files success!"

server = Servers(("192.168.1.154",8880),Handler)
server.serve_forever()
