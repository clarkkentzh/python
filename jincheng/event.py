#coding=utf-8
import threading

e = threading.Event()

e.set()

# wait后没参数就一直等待，除非前面设置e.set()来冲破阻塞
event = e.wait()
# 设置e.set()后则event对象是True
print event     # True

# 清除event对象
e.clear()

# 若是等待时间冲破阻塞，则event是false
event = e.wait(2)
print "这是定时后的event:",event    # false
