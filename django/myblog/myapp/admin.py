# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import *
# Register your models here.

#继承admin，　ModelAdmin用来管理站点应用
class AuthorAdmin(admin.ModelAdmin):
    #显示列表
    list_display = ('first_name','last_name','email')
    #增加一个搜索框
    search_fields = ('first_name','last_name')

    #这个类可以引入一些js文件
    class Media:
        js = (
            '/static/js/a.js',
        )

class BookAdmin(admin.ModelAdmin):
    #增加一个过滤器
    list_filter = ('publication_date',)
    #增加一个事件戳
    date_hierarchy = 'publication_date'
    #排序，当他和Book类中的排序冲突时，这里优先
    ordering = ('-publication_date',)
    #显示几项以及顺序
    fields = ('title','author','publisher','price','publication_date')

class PublisherAdmin(admin.ModelAdmin):
    #分两个框显示信息,classes是样式，collapse是可隐藏
    fieldsets = (
    ('基本信息',{'fields':('name','address','city','state_province','country')}),
    ('高级设置',{
        'classes':('collapse',),
        'fields':('website',)
        }),
    )
    #指定要显示的字段
    list_display = ('name','website')
    #设置显示的字段哪些可点击
    list_display_links = ('name',)
    #设置显示的字段可更改,更改和点击不能重复设置
    list_editable = ('website',)
#用来管理站点和数据库
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
