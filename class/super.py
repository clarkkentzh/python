#coding=utf-8

class Father(object):
    def __init__(self):
        self.height = 160
    def about(self,name):
        print "{} is about {}".format(name,self.height)

class Son(Father):
    def __init__(self):
        self.breat = 90
        super(Son,self).__init__()
    def about(self,name):
        print "{} is about {}, she is {}".format(name,self.height,self.breat)
        super(Son,self).about(name)

a = Son()
a.about("diaochan")
print "++++++",a.__dict__
super(Son,a).about("haha")
