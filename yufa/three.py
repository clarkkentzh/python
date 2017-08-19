#!/usr/bin/python3
#coding=utf-8

i = 0
while i < 3:
    a = input("请输入0-9的任意数")
    b = 5

    if a == b:
        print "恭喜你猜对了"
        break
    elif a < b:
        print "抱歉，你猜小了"
    else :
        print "抱歉，你猜大了"
    i += 1
print "游戏结束"
