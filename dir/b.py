#coding=utf-8
def fun():
    print "这是文件b的方法"

s = 52

class A():
    def __init__(self,name):
        self.name = name
    def fun1(self):
        print "这是b文件的类里的方法"

def _B():
    print "受保护的类"
