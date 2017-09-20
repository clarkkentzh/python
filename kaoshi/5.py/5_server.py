#coding=utf-8
import MySQLdb
from SocketServer import *
import socket,sys

db = MySQLdb.connect("localhost","root","123456","zhao")
cur = db.cursor()
class Servers(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print ("已建立连接：",addr)
        while True:
            data1 = self.request.recv(1024)
            data = data1.split(" ")
            if data[0] == "1":
                cur.execute("select * from user where name = '%s'"%data[1])
                datas = cur.fetchone()
                if data[2] == datas[2]:
                    self.request.send("r")
                else:
                    self.request.send("e")
            elif data[0] == "2":
                print "------------------------------"
                print data
                try:
                    cur.execute("insert into user (name,pa,flog) values('%s','%s',%d)"%(data[1],data[2],int(data[3])))
                    db.commit()
                except Exception as e:
                    db.rollback()
                    self.request.send(e)
                else:
                    self.request.send("yes")
            elif data[0] == "3":
                break
            else:
                print "input is %s"%data[0]
                self.request.send("等待输入")

server = Servers(("192.168.1.154",8880),Handler)
server.serve_forever()
