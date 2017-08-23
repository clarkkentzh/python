#coding=utf-8
from time import ctime,sleep
import os
import threading

def music(i1):
    print "这是第一个线程%s,1的id:%s"%(i1,os.getpid())
    sleep(2)
def funcs(i2):
    sleep(5)
    print "这是第二个线程%s,2的id:%s"%(i2,os.getpid())

threads = []
t1 = threading.Thread(target = music,args = ("clark",))
t2 = threading.Thread(target = funcs,args = ("kent",))

threads.append(t1)
threads.append(t2)
if __name__ == "__main__":

    for t in threads:
# 守护线程,True时主线程不用等子线程结束才结束，直接就能结束，False只有等子线程结束后主线程才能结束
        t.setDaemon(True)
        t.start()

# 设置守护线程时使用join方法会有所冲突
# thread.join()在子线程完成运行之前，该子线程的父线程（一般就是主线程）将一直存在，也就是被阻塞
    # t.join()
    # for t in threads:
    #     t.join()

    print "主线程结束"
