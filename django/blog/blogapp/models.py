# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avater = models.ImageField(max_length = 200,blank = True,null = True,verbose_name = "Head_portrait")
    mobile = models.CharField(max_length = 11,blank = True,null = True,verbose_name = "tel")
    class Meta:
        verbose_name = "User"
        ordering = ['-id']
    def __unicode__(self):
        return self.username

# class user(models.Model):
#     username = models.CharField(max_length = 30)
#     sex = models.CharField(max_length = 30)
#     age = models.IntegerField()
#     email = models.EmailField(blank = True,verbose_name = 'e-mail')

class title(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 2000)
    time = models.CharField(max_length = 50)
    tag = models.CharField(max_length = 5)
    def __unicode__(self):
        return self.title
