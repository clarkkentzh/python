#coding=utf-8

class Zhao():
    def __enter__(self):
        print "enter ********"
    def __exit__(self,type,value,traceback):
        print "exit++++++++++"

# with语句会在结束后将对象删除
with Zhao() as a:
    print "center -------"
