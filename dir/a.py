#coding=utf-8
import b             # 导入模块
#import b as B       # 用B代替b模块名字，模块名较长的时候比较方便
#import b,c          # 可以同时导入多个模块
# from b import A,fun,s,_B    # 直接将b模块的命名空间改在本地，可以直接用这些变量，不用b.，缺点是不能再重复命名其他变量,还可以用from b import *,但是*这个方法不能导入b模块内的受保护的成员类似名字前有一个下划线 _A
from b import *
print b.s
b.fun()
a = b.A("哈哈")
print a.name
a.fun1()

b._B()


#  导入包，就是目录************************************
# 导入的目录必须在目录下面建一个__init__.py文件，多层目录必须建多个，可以什么都不写，但写的语句会在导入包的时候被自动调用,并且就算导入的是下层的目录，只要经过这个目录就会调用
print "**************目录****************"

# 这是一种写法
# import dir1.dir11.d
# dir1.dir11.d.dir11()

# 2 在__init__.py文件中引用的模块可以通过一个__all__　＝　列表　，在列表内将模块名或者属性方法名以字符串格式写入，就可以被导入到此，导入的时候不用精确到__init__文件，只要在其目录即可

from dir1.dir11 import d
from dir1.dir11 import ctime   # 这就是__init__.py里的一个方法
from dir1 import fun          # 这也是
from dir1 import c
c.dir1()
d.dir11()
print ctime()
fun()
