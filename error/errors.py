#coding=utf-8

# 一种写法+++++++++++++++++++++++++++++++
a = raw_input()
b = raw_input()

def fun(a,b):
    try:
        return int(a) / int(b)
    except ValueError,e:
 # 错误信息都是自己手写的，真正的信息可以在错误类型后面加个参数,就像e，打印e,python3必须用as e,和下面相同
        print e.args
        # print "这个应该是int强转字符的时候的错误 ValueError"
    except ZeroDivisionError as e:
        print e
        # print "除数不能为0 错误"

s = fun(a,b)
print s


# 第二种写法+++++++++++++++++++++++++++++
def fun1(a,b):
    try:
        return a / b
# 多个异常可以用多个except，也可以用元组写一起，也可以写Exception
# 这里是TypeError，因为a,b输入的都是字符串格式
    except Exception,e:
        print e
        # print "这是包含所有错误的写法"

print "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
s1 = fun1(a,b)
print s1
