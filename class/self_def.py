#coding=utf-8


# 私有变量和方法格式__name和__fun()，类外部访问不到，只有在类内部可以访问，所以只有在类内部定义方法访问或者修改私有变量和方法
# class Father(object):
#     def __init__(self):
#         self.__name = "moren"
#     def __fun(self):
#         print "这是私有方法"
#     def setname(self,name):
#         if len(name) >= 6:
#             self.__name = name
#         else :
#             self.__fun()
#     def getname(self):
#         print "这是私有属性：{}".format(self.__name)
#
# t = Father()
# t.setname("zhao")
# t.getname()   # 这是私有方法　这是私有属性：moren
#
# # 这里可以证明私有方法和变量是可以继承的
# class Son(Father):
#     pass
#
# t1 = Son()
# t1.setname("hahahahahha")
# t1.getname()  # 这是私有属性：hahahahahha

class Father(object):
    def __init__(self):
        self.__name = "moren"
    def __fun(self):
        print "这是私有的方法"
# 装饰器
    @property
    def name(self):
        return "这是私有的属性：{}".format(self.__name)
    @name.setter
    def name(self,value):
        if len(value) >= 6:
            self.__name = value
        else :
            self.__fun()


t = Father()
t.name = "zh"
print t.name























        ##
