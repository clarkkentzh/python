from socket import *
from select import *
from time import ctime
s = socket()
s.bind(("192.168.1.154",8880))
s.listen(2)

inputs = [s]

while True:
    rs,ws,es = select(inputs,[],[])
    for r in rs:
        if r  is s:
            connfd,addr = r.accept()
            print "recv:",addr
            inputs.append(connfd)
        else:
            try:
                data = r.recv(1024)
                if not data:
                    inputs.remove(r)
                    r.close()
                print "recv:",data
                r.send(ctime())
            except Exception as e:
                print e


s.close()
