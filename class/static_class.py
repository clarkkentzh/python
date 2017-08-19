#coding=utf-8

# １
class Static(object):
    def fun():
        print "这是静态方法"
    funs = staticmethod(fun)

class Classs(object):
    def fun(cls):
        print "这是类方法"
        print "类是：",cls.__name__
    fun1 = classmethod(fun)

Static.funs()
Classs.fun1()

a = Static()
a.funs()

b = Classs()
b.fun1()

# 2 类方法
# class Classs(object):
#     col = (0,0,0)
#     @classmethod
#     def value(cls):
#         if cls.__name__ == "Red":
#             cls.col = (255,0,0)
#         elif cls.__name__ == "Green":
#             cls.col = (0,255,0)
#         return cls.col
#
# class Red(Classs):
#     pass
# class Green(Classs):
#     pass
# class Colors(Classs):
#     pass
#
# red = Red()
# green = Green()
# cols = Colors()
#
# print "red",red.value()
# print "green",green.value()
# print "colors",cols.value()
