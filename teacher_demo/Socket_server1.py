#!/usr/bin/python

#forking
from socketserver import *
from time import ctime

class Server(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('got connection from',addr)
        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            self.request.send(('[%s] :%s'%(ctime(),data)).encode())

server = Server(('127.0.0.1',9999),Handler)

server.serve_forever()
