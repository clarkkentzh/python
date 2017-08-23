from multiprocessing import Pool
import os,time

def funs(i):
    time.sleep(1)
    print 100 + i
    return 100 + i

def funs1(arg):
    print "callback:",arg,os.getpid()

# 创建进程池，可以方５个进程
pool = Pool(5)

for i in range(10):
    # 同步执行所有进程
    # pool.apply(func = funs,args = (i,))

    #异步,一次同时执行５个进程
    pool.apply_async(func = funs,args = (i,),callback = funs1)


pool.close()
pool.join()
