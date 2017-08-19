#coding=utf-8
import traceback
class Zhao(Exception):
    pass

a = raw_input()
try:
    if a == "":
        print "空对象"
        raise Zhao("异常信息")
    print "正常输出：",a
except Zhao as e:
    traceback.print_exc()
    print "*************",e.args
