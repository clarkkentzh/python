# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from forms import *
from myapp.models import Author,Book
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required,permission_required
from usr.models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import os
from django.conf import settings

# Create your views here.
def index(request):

    return render(request,'form.html',{})

def search_form(request):
    print request.method
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return HttpResponse('i hage get %s'%q)
    else:
        return render(request,'form.html',{})

def form_post(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')

        if not request.POST.get('email',''):
            errors.append('Enter a email')

        if not request.POST.get('message',''):
            errors.append('Enter message')

        if not errors:
            return redirect('/form_post/thanks')
    return render(request,"form1.html",{'errors':errors,'subject':request.POST.get('subject'),'email':request.POST.get('email'),'message':request.POST.get('message')})

def thanks(request):
    print "come on"
    print request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_request(request):
    scheme = request.scheme
    body = request.body
    path = request.path
    method = request.method
    content = request.content_type
    get = request.GET
    post = request.POST
    cookies = request.COOKIES
    meta = request.META
    addr = request.META['REMOTE_ADDR']

    print request.get_host()
    return render(request,'request.html',locals())

def formtest(request):
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            print cd['subject']
            print cd['mail']
            print cd['topic']
            print cd['message']
            print cd['cc_myself']
            return HttpResponseRedirect('/formtest')
    else:
        form = RemarkForm()

    return render(request,'formtest.html',{'form':form})

def authorset(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            dic = {'first_name':cd['first_name'],'last_name':cd['last_name'],'email':cd['email']}
            Author.objects.create(**dic)
            return HttpResponseRedirect('/authorform/')
    else:
        form = AuthorForm()

    return render(request,'author.html',{'form':form})

#下面这句和{%csrf_token%}功能相同

# user_info = {
#     'pangzi':{'pwd':"pang123"},
#     'shouzi':{'pwd':'shou123'}
# }
#
# @csrf_exempt
# def login(request):
#     if request.method == "GET":
#         return render(request,"login.html")
#     if request.method == "POST":
#         u = request.POST.get("username")
#         p = request.POST.get("passwd")
#         dic = user_info.get(u)
#         if not dic:
#             return render(request,'login.html')
#         if dic['pwd'] == p:
#             request.session['username'] = u
#             request.session['is_login'] = True
#             #设置存储时间20s
#             request.session.set_expiry(20)
#             return redirect('/index1/')
#         else:
#             return render(request,'login.html')
#
# def index(request):
#     if request.session.get('is_login',None):
#         return render(request,'index1.html',{'current_user':request.session['username']})
#     else:
#         return render(request,'login.html')
#
# def logout(request):
#
#     session = Session.objects.all()
#     print session
#     #清除session
#     request.session.clear()
#     return redirect('/login/')

#######register login logout######################
def thanks(request):
    return HttpResponse("thanks for your register but you not have permission_required")

#第一个参数是设置权限add,delete,change，无权限的话跳转到第二个参数的url
@permission_required('add_User',login_url = '/thanks/')
def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                cd = reg_form.cleaned_data
                User.objects.create(username=cd['username'],password=make_password(cd['password']),email=cd['email'],mobile=cd['tel'],avatar = cd['avatar'])

                return HttpResponseRedirect("/login/")
            else:
                return render(request,'failure.html',{'reason':reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        print e
    return render(request,'reg.html',locals())

#当是登录状态时，输入login_test会打印这句话，若没有登录会跳转到这个路径
@login_required(login_url = '/login/')
def login_test(request):
    return HttpResponse('thank you for login')

def login(request):
    errors = []
    if request.method == "POST":
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        if not username:
            errors.append('enter a username')
        if not password:
            errors.append('enter a password')
        if not errors:
            #验证user是否合法
            if not request.user.is_authenticated():
                user = auth.authenticate(username = username,password = password)
                if user is not None and user.is_active:
                    #让user登录
                    auth.login(request,user)
                    # return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
                    return HttpResponseRedirect(request.GET.get('next','/'))
                else:
                    return HttpResponse("username or password invalid")
            else:
                return HttpResponse("you have already login")
    return render(request,"user_login.html",{'errors':errors})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def avatar(request):
    images = request.POST.get('avatar','')
    print images
    return render(request,'avatar.html',{})

def page(request):
    article_list = ['a1','a2','a3','a4','a5','a6','a7','a8']
    paginator = Paginator(article_list,5)

    #获取当前页为几页
    p = int(request.GET.get('page',1))

    article_list = paginator.page(p)

    pages = range(1,article_list.paginator.num_pages + 1)
    return render(request,'page.html',locals())

def avatar(request):
    if request.method == "POST":
        myFile = request.FILES.get('avatar',None)
        if not myFile:
            return HttpResponse('no file')
        dest = open(os.path.join(settings.MEDIA_ROOT,myFile.name),'wb+')
        Image.objects.create(avatar = os.path.join(settings.MEDIA_URL,myFile.name))

        for i in myFile:
            dest.write(i)
        dest.close()
        return HttpResponse("upload over")
    return render(request,'avatar.html',{})

def article(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('title',''):
            errors.append('Enter a title')

        if not request.POST.get('desc',''):
            errors.append('Enter a desc')

        if not request.POST.get('content',''):
            errors.append('Enter content')

        if not errors:
            return HttpResponse("Thank you.....")
        else:
            return render(request,"article.html",{'errors':errors,'title':request.POST.get('title'),'desc':request.POST.get('desc'),'content':request.POST.get('content')})

    return render(request,"article.html")
# @csrf_exempt
# def upload(request,dir_name):
#      ##################
#     # 这是kindeditor想要的格式
#     #  kindeditor图片上传返回数据格式说明：
#     # {"error": 1, "message": "出错信息"}
#     # {"error": 0, "url": "图片地址"}
#     ##################
#     result = {"error": 1, "message": "上传出错"}
#     #imgFile来自于附文本编辑器查看源码之后找到的它定义的文件名字
#     files = request.FILES.get("imgFile", None)
#     if files:
#         return HttpResponse('okle')
#     return HttpResponse('error')


import uuid
import json
import datetime as dt
#这个装饰器用于不再进行表单验证提交
@csrf_exempt
def upload(request, dir_name):
    ##################
    # 这是kindeditor想要的格式
    #  kindeditor图片上传返回数据格式说明：
    # {"error": 1, "message": "出错信息"}
    # {"error": 0, "url": "图片地址"}
    ##################
    result = {"error": 1, "message": "上传出错"}
    #imgFile来自于附文本编辑器查看源码之后找到的它定义的文件名字
    files = request.FILES.get("imgFile", None)
    if files:
        result =image_upload(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")

#目录创建
def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    dir_name = dir_name + '/%d/%d/' %(today.year,today.month)
    if not os.path.exists(settings.MEDIA_ROOT + dir_name):
        os.makedirs(settings.MEDIA_ROOT + dir_name)
    return dir_name

# 图片上传
def image_upload(files, dir_name):
    #允许上传文件类型
    allow_suffix =['jpg', 'png', 'jpeg', 'gif', 'bmp']
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {"error": 1, "message": "图片格式不正确"}

    relative_path_file = upload_generation_dir(dir_name)

    path=os.path.join(settings.MEDIA_ROOT, relative_path_file)

    if not os.path.exists(path): #如果目录不存在创建目录
        os.makedirs(path)

    file_name=str(uuid.uuid1())+"."+file_suffix
    path_file=os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path_file + file_name
    #写入操作，二进制形式，最终完成上传，真正保存图片
    open(path_file, 'wb').write(files.file.read())
    return {"error": 0, "url": file_url}

#设置缓冲时间,第二种，针对页面设置缓冲
# from django.views.decorators.cache import cache_page
#
# @cache_page(10)
def cache(request):
    import time
    ctime = time.time()
    return render(request,'cache.html',{'ctime':ctime})
