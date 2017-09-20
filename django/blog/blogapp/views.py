# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import time
from models import *
from forms import *
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib.sessions.models import Session
# Create your views here.

name = "wait"
def page(request,datas):
    paginator = Paginator(datas,3)

    #获取当前页为几页
    p = int(request.GET.get('page',1))

    datas = paginator.page(p)

    return datas


def mainpage(request,datas):
    if datas:
        data = int(datas)
        if data == 1:
            page = 1
            databases = title.objects.all()

            paginator = Paginator(databases,3)
            #获取当前页为几页
            p = int(request.GET.get('pags',1))
            articles = paginator.page(p)

            pages = range(1,articles.paginator.num_pages + 1)

            return render(request,"mainpage.html",locals())
        elif data == 2:
            page = 2
            databases = title.objects.filter(tag = "s")
            paginator = Paginator(databases,3)
            #获取当前页为几页
            p = int(request.GET.get('pags',1))
            articles = paginator.page(p)

            pages = range(1,articles.paginator.num_pages + 1)
            return render(request,"mainpage.html",locals())
        elif data == 3:
            page = 3
            databases = title.objects.filter(tag = "t")
            paginator = Paginator(databases,3)
            #获取当前页为几页
            p = int(request.GET.get('pags',1))
            articles = paginator.page(p)

            pages = range(1,articles.paginator.num_pages + 1)
            return render(request,"mainpage.html",locals())
    else:
        page = 11
        return render(request,"mainpage.html",locals())



def myself(request):
    page = 10
    if name == 'wait':
        return HttpResponseRedirect('/')
    names = request.session['username']
    print name
    users = User.objects.filter(username = name)
    return render(request,"mainpage.html",locals())

def write(request):
    page = 12
    if request.method == 'POST':
        times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        title.objects.create(title = request.POST.get('title'),content = request.POST.get('content'),time = times,tag = request.POST.get('lei'))
    return render(request,'mainpage.html',locals())

def look(request):
    page = 13
    datas = request.GET.get("ids","")
    if datas:
        databases = title.objects.get(id = datas)
    return render(request,'mainpage.html',locals())
def reg(request):
    a = 0
    try:
        if request.method == 'POST':
            username = request.POST.get("username",'')
            password = request.POST.get("password",'')
            email = request.POST.get("email",'')
            if username:
                dic = {
                'username':username,
                'password':make_password(password),
                'email':email
                }
                User.objects.create(**dic)

                return HttpResponseRedirect("/")
            else:
                return render(request,'login.html',{'reason':reg_form.errors})
        else:
            return render(request,'login.html',locals)
    except Exception as e:
        print e
    return render(request,'login.html',locals())

def login(request):
    a = 1
    if request.method == "POST":
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")

        #这是判断用户没有登录
        if not request.user.is_authenticated():
            user = auth.authenticate(username = username,password = password)
            if user is not None and user.is_active:
                #这里是让user登录
                auth.login(request,user)
                request.session['username'] = username
                global name
                name = request.session['username']
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
                # return HttpResponseRedirect(request.GET.get('next','/'))
                return HttpResponseRedirect('/page/')
            else:
                return HttpResponse("username or password invalid")
        else:
        #这里是已经存在登录的账号，存在就直接进入主页面
            global name
            name = request.session['username']
            return HttpResponseRedirect("/page/")
    return render(request,"login.html",locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
