import threading
import time

# 多个线程(或者多个进程)间为避免操作共同资源的影响，可以用Lock避免冲突
a = 1

#当没有锁的时候线程的运行是先fun1然后到time.sleep(1)的时候fun1线程暂停，执行fun2线程，所以两次的a 都为100，上锁的时候，如果fun1没有解锁操作，会一直执行线程fun1,直到结束然后执行线程fun２,到线程fun2的lock.acquire（）会始终阻塞在这，所以一个线程上锁之后执行完之后需要有解锁操作

def fun1():
    # 锁住线程
    lock.acquire()
    global a
    a = 10
    time.sleep(1)
    print "fun1 a = :%s\n"%a
    lock.release()

def fun2():
    lock.acquire()
    global a
    a = 100
    print "fun2 a = :%s\n"%a
    lock.release()

# 全局锁对象
lock = threading.Lock()

t1 = threading.Thread(target = fun1)
t2 = threading.Thread(target = fun2)

# 启动线程，有点先后顺序
t1.start()
t2.start()
