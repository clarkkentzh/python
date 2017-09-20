#coding=utf-8

from django.conf import settings
def globals(request):
    site = "hahahahahaha"
    tel = "18810207835"
    email = "lvze_work@126.com"
    basedir = settings.BASE_DIR
    return locals()
