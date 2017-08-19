#coding=utf-8

# ******************************普通装饰器
# def deco(fun):
#     def func():
#         print "加上这一句"
#         fun()
#     return func
# @deco
# def fun():
#     print "最开始这一句"
#
# # f = deco(fun)
# fun()


# *********************
# def deco(fun):
#     def func(a):
#         if a != "外层":
#             ret = "外层" + a
#             fun(ret)
#         else :
#             fun(a)
#     return func
#
# @deco
# def fun(a):
#     print a
#
# fun("外层")

# *****************************
def deco(arg):
    def _deco(fun):
        def __deco(a,b):
            ret = fun(a,b)
            s = ret ** arg
            print s
        return __deco
    return _deco

@deco(2)
def fun(a,b):
    return a + b
fun(1,2)

##
