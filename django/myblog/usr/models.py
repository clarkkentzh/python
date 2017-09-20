# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/%Y/%m",default = "static/default.png",max_length = 200,blank = True,null = True,verbose_name = "Head_portrait")
    mobile = models.CharField(max_length = 11,blank = True,null = True,verbose_name = "tel")
    class Meta:
        verbose_name = "User"
        ordering = ['-id']
    def __unicode__(self):
        return self.username

class Image(models.Model):
    avatar = models.ImageField(upload_to="avatar/%Y/%m",default = "static/default.png",max_length = 200,blank = True,null = True,verbose_name = "Head_portrait")
