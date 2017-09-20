import gevent,sys,urllib2
from gevent import monkey;monkey.patch_all()
# 由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成

def fun1():
    print "run in fun1"
    res = urllib2.urlopen("http://www.baidu.com")
    data = res.read()
    print "switch fun1 agin",len(data)

def fun2():
    print "run in fun2"
# 这是人为的阻塞操作
    gevent.sleep(4)
    print "switch fun2 agin"

f1 = gevent.spawn(fun1)
f2 = gevent.spawn(fun2)

gevent.joinall([f1,f2])

#*****************************************************************
# def f(n):
#     for i in range(n):
#         print gevent.getcurrent(),i
#         # gevent.sleep(0)
#
# g1 = gevent.spawn(f,5)
# g2 = gevent.spawn(f,5)
# g3 = gevent.spawn(f,5)
#
# gevent.joinall([g1,g2,g3])
