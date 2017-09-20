#coding=utf-8
from django.utils.deprecation import MiddlewareMixin

#这个类Row继承这个父类，内部的两个函数名固定，参数也固定
class Row(MiddlewareMixin):
    def process_request(self,request):
        print 11111111111111

    def process_response(self,request,response):
        print 222222222222222
        return response
