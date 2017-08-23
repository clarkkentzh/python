#coding=utf-8

class Zhao(object):
    age = 20
    def __init__(self,name):
        self.name = name
    def ages(self,num):
        self.age = self.age + num

# ages是自定义的方法，调用后会改变对象的age
first = Zhao("ha")
print first.age    # 20
first.ages(3)
print first.age    # 23
print first.name   # ha
# __init__是类自带的方法，self是每个方法都必须有的形参，但是它不接受实参，只是用来指定this，实参有self后面的形参来接收,在这里__init__可以给对象设置一个name属性，值为传来的实参
two = Zhao("zhao")
three = Zhao("hong")
print two.name      # zhao
print three.name    # hong

print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
# 给类对象增加私有方法

def fun(self):
    print "这是私有方法"
#1 用类直接将方法定为一个属性，但是这不是私有的
Zhao.fun = fun
two.fun()
three.fun()

#2 直接用对象将方法定为一个属性，但是调用时得传一个让self接收的值
two.f = fun
two.f(-1)


#3 用新模块方法创建私有变量
import new
two.f = new.instancemethod(fun,two,Zhao)
two.f()
