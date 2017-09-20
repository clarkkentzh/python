#!/usr/bin/env python
#coding=utf8

#多线程服务器处理图像
#吕泽 2017-6-13
#python 2.7.11
#所需第三方库:MySQLdb,PIL

import threading
import SocketServer
import sys
import time
import struct
#import MySQLdb
import os,shutil
from random import randint
#from PIL import Image

#线程处理类,具体执行图像处理内容
class ThreadTCPRequestHander(SocketServer.BaseRequestHandler):

    #图片格式转化jpg->bmp
    def imageConvert(self,path):
        im = Image.open(path)
        path.replace(".jpg",".bmp")
        im.save(path)

    #算法调用
    def arith(self,path):
        return "The result " + path

    #结果反馈
    def sendResult(self,result):
        dataSize = len(result)
        msg = struct.pack("ii",1001,dataSize)
        self.request.sendall(msg + result)

    #数据库存储信息
    def dataBaseStorage(self):
        pass

    #本地存储图片
    def localStorage(self,data):
        #self.imageConvert(path)
        #result = self.arith("this is image path")
        #self.dataBaseStorage()
        #self.sendResult(result)

        shutil.move("./images/image.jpg","./images/dir")
        os.rename("./images/dir/image.jpg","./images/dir/{}.jpg".format(randint(1,10000)))

    #接收图片
    def picRecv(self,data):
        path = "./images/image.jpg"
        try:
            fd = open(path,'ab')
        except:
            print "create image failed"

        fd.write(data)
        fd.close()


    #接收消息，根据前四个字节判断消息行为，调用相应函数
    def msgChoice(self):
        choice = {1000:self.picRecv,1001:"return the handle result",1002:self.localStorage}

        self.data = self.request.recv(4096)
        if len(self.data) >= 8:
            dataType,dataSize = struct.unpack("ii",self.data[0:8])
            print "dataType:{},dataSize:{},data:{}".format(dataType,dataSize,self.data[8:8 + dataSize])
            choice.get(dataType)(self.data[8:8+dataSize])

    #自动化执行函数
    def handle(self):
        while True:
            self.msgChoice()

#多线程服务器创建,使用SocketServer模块实现.SocketServer 将多线程tcp服务器实现过程进行封装
class ThreadTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass


#启动服务器,持续运行,设置为守护线程
def startServer():
    HOST,PORT = sys.argv[1],int(sys.argv[2])
    server = ThreadTCPServer((HOST,PORT),ThreadTCPRequestHander)
    ip,port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.name = "StartThread"
    server_thread.daemon = True
    server_thread.start()

    print "Server loop running in thread:{},server ip:{},port:{}".format(server_thread.name,ip,port)


if __name__ == "__main__":
    startServer()
    while True:
        time.sleep(3)
        print "Waiting for client picture."
