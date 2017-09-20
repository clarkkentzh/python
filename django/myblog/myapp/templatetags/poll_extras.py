from django import template

register = template.Library()

@register.filter(name = "myfilter")
def myfilter(value,arg):
    return value.replace(arg,"#")
