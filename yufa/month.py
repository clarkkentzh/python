#!/usr/bin/python3
#coding=utf-8

ping = 0
days = 0

mons = [31,28,31,30,31,30,31,31,30,31,30,31]

a = raw_input("输入日期,类似2016-1-1: ")
b = a.split("-")
year = int(b[0])
mon = int(b[1])
day = int(b[2])

print "你输入的日期为%d年%d月%d日"%(year,mon,day)
if year < 0  or mon < 1 or mon > 12 or day < 0 or day > 31:
    print "输入有误"
    exit()
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    ping = 1
    if mon == 2 and day > 29:
        print "输入有误"
        exit()
elif mon == 2 and day > 28:
    print "输入有误"
    exit()
if mon == 2 or mon == 4 or mon == 6 or mon == 9 or mon == 11:
    if day > 30:
        print "输入有误"
        exit()
for i in range(0,mon - 1):
    days += mons[i]

days += day
if mon > 2:
    days += ping
print "days = %d"%days
