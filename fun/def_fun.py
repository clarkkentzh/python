#coding=utf-8


# *************函数定义形参的设置方式**************

# 普通的位置传参
def funs(a,b):
    print "a = : ",a,
    print "b = : ",b
funs(10,20)

# b设置了默认值,有参数则是参数的值，没有就是默认值，这种格式必须写在形参后面
def fun(a,b = 100):
    print a,b
fun(1)

# *c是收集数据的方式，并把收集的参数合为元组，不能收集c = 10的格式，数字，字符串都可以
# *c也必须写在形参后面,也可以加上默认值传参
def fun1(a,b = 200,*c):
    print a,b,c

fun1(1,2,3,4,5)


# **d也是收集参数，并合为字典形式，但实参必须是键值对即c = 10,d = 30的格式
def fun2(a,b = 300,*c,**d):
    print a,b,c,d
fun2(1,e = 2,f = 3)



# ***************python3中元组传参方式******************************
def fun3(a,*b,c):
    print (a,b,c)
fun3(1,2,3,4,c = 5)
