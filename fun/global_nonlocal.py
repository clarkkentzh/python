#coding=utf-8

# global
# 用来在函数或其他局部作用域中使用全局变量,主要是使用后可以在局部作用域内修改变量
# a = 10
# def fun():
#     global a
#     a += 1
#     print "内部：",a
# fun()
# print "外部：",a


# nonlocal是python3的关键字,和global类似，但是nonlocal是指内层函数可以修改外层函数的（非全局）变量

def fun():
    a = 32
    def son():
        nonlocal a
        a += 1
        print (a)
    return son
t = fun()
t()
