#coding=utf-8

#  匿名函数立即调用,x为形参,冒号后面为返回值
print (lambda x:x+1)(1)
print (lambda a,b,c:a+b+c)(5,3,4)

# ***赋值调用
l = [lambda x:x ** 2,lambda x:x ** 3,lambda x:x ** 4]

for f in l:
    print f(3)
