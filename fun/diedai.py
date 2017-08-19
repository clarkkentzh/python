#coding=utf-8

# 自定义迭代器
class Zhao(object):
    def __init__(self,arg):
        self.arg = arg
    def __next__(self):
        self.arg += 1
        return self.arg

a = Zhao(1)
print a.__next__()
