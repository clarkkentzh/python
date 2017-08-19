#coding=utf-8

# 闭包,内部函数有权访问外部函数的变量的函数称为闭包,优点可以保证变量的私有化,保护空间不受污染
def fun(n):
    a = 10
    def son(m):
        return n ** m
    return son
f = fun(2)
print f(3)
