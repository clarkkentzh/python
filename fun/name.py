#coding=utf-8
name = raw_input("输入名字:")

def first(arg):
    def two(fun):
        def three(name):
            if 4 <= len(name) <= 8:
                ret = "正确"
                print ret
            elif len(name) < 4:
                ret = "太短了 " + arg
                print ret
            elif len(name) > 8:
                ret = "太长了" + arg
                print ret
        return three
    return two

@first("moren")
def fun():
    return
fun(name)
