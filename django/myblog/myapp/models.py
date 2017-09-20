# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# class BetterCharField(models.Field):
#     def __init__(self,length,*args,**kwargs):
#         self.length = length
#         super(BetterCharField,self).__init__(*arg)
#     def db_type(self,connection):
#         return 'char(%s)'%self.length
# class MyModel(models.Model):
#     my_field = BetterCharField(25)



class BookQuerySet(models.QuerySet):
    def little(self):
        return self.filter(id__lt = 4)
class BookManager(models.Manager):
    # def get_queryset(self):
    #     return BookQuerySet(self.model,using = self)

    def title_count(self,keyword):
        return self.filter(title__icontains = keyword).count()

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length = 30,verbose_name = "姓名")
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField(verbose_name = "网址")

    #设置查询内容对外显示的文字
    def __unicode__(self):
        return self.name
    # ordering是排序方式，按什么排序
    class Meta:
        #数据表显示的名字
        verbose_name = "出版社"
        verbose_name_plural = verbose_name
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

    email = models.EmailField(blank = True,verbose_name = 'e-mail')
    def __unicode__(self):
        return u"%s %s"%(self.first_name,self.last_name)
    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name
        ordering = ['first_name']

class Book(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField(default = 0.0)
    publication_date = models.DateField(blank = True,null = True)
    publisher = models.ForeignKey(Publisher)
    author = models.ManyToManyField(Author)
    objects = BookManager()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = verbose_name
        ordering = ['id']
