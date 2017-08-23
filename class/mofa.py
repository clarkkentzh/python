#coding=utf-8
'''这是为了测试整个文档的一句话 hahahahahahaha'''
class Zhao(object):
    '''这是测试doc方法的一句话'''


#　__init__方法在对象创建的时候调用，但是在__new__方法之后，__new__返回的值就是__init__的参数，就是创建的对象
    def __init__(self):
        print "这是init 方法"
        self.name = "bianliang"
        self.dict = {}

# __new__ 方法在创建类对象的时候被调用，其返回值就是对象,没有该方法，则默认父类的该方法
    def __new__(cls):
        print "这是new 方法"
        return super(Zhao,cls).__new__(cls)

# __call__ 方法定义后对象可以当成函数一样调用时，触发这个方法
    def __call__(self,str):
        print "定义了call方法",str

# __del__　删除对象时触发
    def __del__(self):
        print "del方法触发"

# 此函数是在打印属性变量的时候调用
    def __getattr__(self,name):
        print 'You use getattr on attr %s'%name
        return

# 此方法在给属性变量赋值的时候调用，如果没有这个属性变量则创建这个属性
# __dict__是类的属性组成的字典，将name名为键，value为值,是设置属性的一步
    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value

# 此方法是在删除属性的时候调用
    def __delattr__(self,name):
        print "You use delattr"

# 类似上面三种
    def __getitem__(self,key):
        return self.dict[key]

    def __setitem__(self,key,value):
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)

a = Zhao()  #这里先触发__new__方法,再触发__init__方法，若new方法没有返回对象，则init 方法不会触发
print a.__doc__

a("call")  #这个可以触发__call__方法
# del(a)  #这个可以触发__del__方法
print a.name
print a.__module__

a.value = 90
print a.value
del a.value
print a.__dict__

print "++++++++++++++++"
a["a"] = 1
print a["a"]
print len(a)
