#coding=utf-8

import time

def fun(m):
    a,b = 1,1
    while a < m:
# 普通函数有yield就成了一个生成器，类似一个返回，但是阻塞在这里，执行一次阻塞一次
        yield a
        a,b = b,a + b
        print "++++++"

# 生成器生成一个迭代对象,此对象可以用next()执行生成器并打印yield的值，也可以用send()给yield传送值
t = fun(20)
while True:
    time.sleep(1)
    print t.next()
