#coding=utf-8
import multiprocessing,time,os
from multiprocessing import Queue,Pipe

def worker(time1,p):
    n = 5
    print p.get()
    childs.send([45,64,"world"])
    while n > 0:
        print "********1********"
        print "子进程１　id:",os.getpid()
        time.sleep(time1)
        n -= 1

def teacher(time2,p):
    n = 5
    print childs.recv()
    p.put([45,None,"hello"])
    while n > 0:
        print "********2***********"
        print "子进程２ id:",os.getpid()
        time.sleep(time2)
        n -= 1

if __name__ == "__main__":

# 子进程之间互相传递信息,一个子进程用put发送数据，一个用get接收数据
    ps = Queue()
# 用于父子进程之间传递数据，一个进程用send发送，一个用recv接收
    parents,childs = Pipe()

    parents.send("父亲")
    p = multiprocessing.Process(name = "worker",target = worker,args = (2,ps))
    p.start()
    q = multiprocessing.Process(name = "teacher",target = teacher,args = (3,ps))
    q.start()

    p.join()
    q.join()
    print parents.recv()
    print "p.id:",p.pid
    print "p.name:",p.name
    print "q.id:",q.pid
    print "q.name:",q.name
