#coding=utf-8
import os,sys
import time
from signal import *

pid = os.fork()

if pid < 0:
    print "create process failed"
elif pid == 0:
    pids = os.fork()
    if pids == 0:
        time.sleep(1)
        print "这是孙子进程",os.getpid()
        print "这是孙子的爹的进程",os.getppid()
    elif pids > 0:
        sys.exit()
        print "********",os.getpid()
else:
    # os.wait()      # 解决僵尸进程第一种方法
    # signal(SIGCHLD, SIG_IGN)  #解决僵尸进程第二种方法
    time.sleep(1)

    print "parent id",os.getpid()
    print "child pid",pid
    while True:
        pass

# os.system("python mul.py")     # 这句可以执行mul.py文件
print "**************fork******************"
