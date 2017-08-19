#coding=utf-8

import traceback
# python3 里面错误信息的e必须用as 这种格式，else,finally 的内容必须在return 之前
def fun(a,b):
    c = None
    try:
        c = a / b
    except TypeError as e:
# traceback也是打印错误信息，信息更详细，需要先引用模块,可以这句赋给变量然后打印变量
        # traceback.print_exc()
# 参数是将错误信息打印到一个文件内
        traceback.print_exc(file = open("try.text","a+"))
        # print (e)
    except ZeroDivisionError as e:
        traceback.print_exc(file = open("try.text","a+"))
    else:
        print ("没有错误的时候就打印")
    finally:
        print ("有没有异常都打印")
    return c

s = fun(3,"a")
print (s)
