#coding=utf-8

# 父类的方法和变量都会被子类继承,__init__也会被继承
class Father(object):
    def __init__(self,name):
        self.name = name
    door = 4
    def fun(self):
        print "这是父类的方法"

class Son(Father):
    pass

# 子类在父类的基础上改变变量
class Son1(Father):
    door = 2

# 子类在父类的基础上增加方法,也可以改变父类的方法
class Son2(Father):
    def fun(self):
        print "我在子类里面改变了这个方法"
    def fun1(self):
        print "这是子类的方法"


a = Son("first")
print "a = ",a.door
a.fun()

b = Son1("two")
print "b = ",b.door
b.fun()

c = Son2("three")
print "c = ",c.door
c.fun()
c.fun1()
