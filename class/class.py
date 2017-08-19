#coding=utf-8

class FirstClass(object):
    name = "zhao"
    age = 24
    def fun(self):
        print "这是类里面的方法"
    class Meta():
        sex = "man"

# 通过类名直接修改内部属性变量和属性方法，也可以访问打印
FirstClass.name = "hong"
FirstClass.age = 12
print FirstClass.name
print FirstClass.age

# 通过类创建实例化一个对象来访问变量和方法,上面修改会改变类的原始数据，所以这里也会变化
cls = FirstClass()
print cls.name
print cls.age
cls.fun()

# 也可以通过这个实例化的对象改变属性变量，不会影响其他的对象。
cls1 = FirstClass()
cls1.name = "zhaohong"
cls1.age = 23
print cls1.name
print cls1.age

# 访问类内部的类，需要实例化再实例化内部的类
cls2 = FirstClass().Meta()
# meta = cls2.Meta()  # 和上面的写法类似
print cls2.sex
