#coding=utf-8
from django import forms
from blogapp.models import User,title

TOPIC_CHOICES = (
    ('a','新闻'),
    ('t','旅游'),
    ('s','技术'),
)

class RemarkForm(forms.Form):
    title = forms.CharField(max_length = 100,label = '标题')
    content = forms.CharField(label = '内容',widget = forms.Textarea)
    time = forms.CharField(max_length = 50,label = '时间')
    tag = forms.ChoiceField(choices = TOPIC_CHOICES,label = '类别')
