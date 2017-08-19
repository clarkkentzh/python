#coding=utf-8
print "访问下层这个会不会调用,会"

from time import ctime
def fun():
    print "init里的方法"
__all__ = ["ctime","fun"]
