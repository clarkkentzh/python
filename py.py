#!/usr/bin/python3
#coding=utf-8




# print "哈哈哈哈"
print ("哈哈哈哈")   #python3需要加括号


print ('''hello
      world''')      #三引号保存换行格式

a = "123"
b = int(a)
c = hex(b)
print (type(a))        #<class 'str'>
print (type(b))        #<class 'int'>
print (type(c))        #<class 'str'>
print(a)         # 123
print(b)         # 123
print(c)         # 0x7b

f = 10.0
e = 3.0
print (f / e)    # python结果是3
print (f / e)    # python3 结果是3.333333333333
# 当f和e赋值时有小数点位，则两种python的结果都是3.3333333333,python3略有不同

# 输入input,字符串raw_input,在３里面没有raw_input,但input和raw_input效果一样
# a1 = input()
# b1 = input()
#
# print a1,b1
#
# c1,d1 = input()
#
# print c1,d1


with open("text.text","w+") as fd:
    # print >> fd,"hello world"      
    print ("nihaoa",file = fd)       # 3的写法，不用>>
