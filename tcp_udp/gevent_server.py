import gevent
from gevent import monkey;monkey.patch_all()
from socket import *
from time import ctime

def server():
    ADDR = ("192.168.1.154",8880)
    s = socket()
    s.bind(ADDR)
    s.listen(10)
    while True:
        connfd,addr = s.accept()
        print "connect from ",addr
        gevent.spawn(handler,connfd)

def handler(connfd):
    try:
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            print "recv:",data
            connfd.send(ctime())
    except Exception as e:
        print e
    finally:
        connfd.close()

if __name__ == "__main__":
    server()
