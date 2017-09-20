# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import loader
import datetime
from django.db.models import F,Q
from django.db import connection

#引用数据库的类
from models import *

#模板的html文件系统会自动的在templates这个固定名字目录下调用
# Create your views here.
def hello(request):
    return HttpResponse("这是我的第一个Django项目")

#类似渲染页面
def get_html(request):
    now = datetime.datetime.now()

    #模板一种方法
    # html = "<html><body>这是时间%s</body></html>"%now

    #加载模板 二
    # t = loader.get_template("time.html")
    # html = t.render({"date":now})
    # return HttpResponse(html)

    #模板　三
    # return render_to_response("time.html",{"date":now})

    #模板　四　最常用方法 request是固定的,只要和函数的参数一致就行
    return render(request,"time.html",{"date":now})

#调转页面
def jump(request):
    #在页面上设置点击按钮点击跳转页面
    # return render(request,"jump.html",{})

    #重定向跳转 两种写法
    # return HttpResponseRedirect("/myapp/time")
    # return redirect("/myapp/time")
    return redirect("http://www.baidu.com")

def error(request):
    raise Http404()

#url给模板views传参数,a和b是由url设置的第三个参数字典内的值
def argument(request,a,b):
    print a
    print b
    if a > b:
        return HttpResponse("a > b")
    else:
        return HttpResponse("a <= b")
#第二中传参方式，a,b,c分别对应url里括号里面的内容，名字必须对应
def argument1(request,a,b):
    print a
    print b
    return HttpResponse("get arguemnt1")

#views给页面传参数,可以传变量，列表，元组，字典，函数，类
def template(request):
    a = 10
    b = [1,2,3,54]
    c = {"ha":"hello","haha":65}
    def fun(strs):
        return "hello %s"%strs
    class clark(object):
        age = 24
    obj = clark()
    return render(request,"template.html",{"a":a,"b":b,"c":c,"d":fun("zhaohong"),"e":obj})

def tag(request):
    a = -6
    b = [2,3,4,5]
    c = {"a":"zhao","b":"hong","c":"clark"}
    return render(request,"tag.html",locals())

def filter(request):
    a = "hello"
    b = 1
    c = "hello world"
    return render(request,"filter.html",locals())

def extend(request):
    return render(request,"base1.html",{})

def include(request):
    return render(request,"include1.html",{})

def static(request):
    return render(request,"static.html",{})

def globa(request):
    return render(request,"globa.html",{})


#数据库的操作
def add_data(request,table):
    #三种增加方式
    if table == "author":
        Author.objects.create(first_name = "zhao",last_name = "hong",email = "clarkkent.z@126.com")
    elif table == "book":
        obj = Book(title = "Mysql database",
        publication_date = datetime.datetime.now(),
        publisher_id = 1)
        obj.save()
    else:
        dic = {
        'name':"人民出版社",
        'address':'颐和山装',
        "city":'北京',
        'state_province':'山西',
        "country":'china',
        "website":"www.baidu.com"}
        Publisher.objects.create(**dic)

    return HttpResponse("add data ok")

def del_data(request):
    Book.objects.filter(id = 1).delete()
    return HttpResponse("delete ok")

def update_data(request):
    # 11　　查到可以有多条，没有结果返回空列表
    Publisher.objects.filter(id__gt = 1).update(name = "赵宏出版社")
    # 22　get是精确匹配，查到结果只能有一条，如果没有会报错
    obj = Book.objects.get(id = 5)
    obj.title = "哈哈哈哈"
    obj.save()

    return HttpResponse("update ok")

def select_data(request):
    #这是所有的书对象
    a = Book.objects.all()
    b = Book.objects.all().values("title")
    c = Book.objects.all().values_list("title","publication_date")

    #
    d = Author.objects.get(id = 1)
    e = Author.objects.exclude(id__lt = 1)

    #F,Q
    #F是使用查询条件的值进行运算
    Book.objects.filter().update(price = F("price") + 10)

    #Q是构造一个搜索条件
    q = Q()

    q.connector = "AND"
    q.children.append(('id',1))
    q.children.append(('last_name','hong'))

    f = Author.objects.filter(q)

    g = Book.objects.title_count("Mysql")
    return render(request,"select.html",locals())

def foreign(request):
    book = Book.objects.get(id = 2)
    #1对多
    p = book.publisher
    #多对多
    author_list = book.author.all()

    #反向多对一，多对多查询
    pub = Publisher.objects.get(id = 1)
    book_list = pub.book_set.all()

    auth = Author.objects.get(id = 2)
    book_list1 = auth.book_set.all()
    return render(request,'select.html',locals())

def sql(request):
    #查询
    sql = '''select * from myapp_author'''
    author_list = Author.objects.raw(sql)[0]

    #增删改查
    with connection.cursor() as cursor:
        sql = "insert into myapp_author(first_name,last_name,email) values('mo','yan','123@123.com')"
        cursor.execute(sql)

    return render(request,"select.html",locals())









#######
