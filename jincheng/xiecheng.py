from greenlet import greenlet
# 协程

def fun1():
    print "12"
# 这里跳转到线程２执行
    gr2.switch()
    print "34"

def fun2():
    print "56"
    print "78"
# 这里又返回到线程１上次执行的位置
    gr1.switch()

gr1 = greenlet(fun1)
gr2 = greenlet(fun2)

# 首先这里跳转到线程１去执行
gr1.switch()
