#coding=utf-8

class First(object):
    name = "luosifu"
    age = 24

class Two(object):
    name = "zhao"
    sex = "man"

class Three(First,Two):
    pass

# 多重继承相同属性的查找顺序，深度优先算法
a = Three()
print a.name # luosifu
print a.sex

# 这两种都可以查看新式类的继承查找顺序
print Three.__mro__
print Three.mro()


# 判断第一个类是否和第二个类有继承关系，孙子类也可以
print issubclass(Three,Two)  # True


# 判断一个对象是不是某个类的对象
print "++++++++++++++++++++++++++++++++++++"
class Four(object):
    pass

print isinstance(a,First)  # True
print isinstance(a,Three)  # True
print isinstance(a,(First,Two,Three,Four)) # True  用元组也行,但是只要有正确的类就True
print isinstance(a,Four)  # False

# isinstance也可以判断数据类型
n = 1
print isinstance(n,int)  # True


# ****************判断,设置对象的属性******************
print "*************************"
s = First()

# 判断s 这个对象有没有name这个属性
print hasattr(s,"name")  # True

# 获得s对象的属性的值，没有该属性则第三个参数默认为该属性值
print getattr(s,"name")  # luosifu
print getattr(s,"school","beijing") # 北京

# 给s对象设置一个属性和值
setattr(s,"car","www")
print s.car
