#!/usr/bin/python3
#coding=utf-8

#   ***************if判断大小,排序***************
# a = input()
# b = input()
# c = input()
# if a > b:
#     sl = a
#     a = b
#     b = sl
# if a > c:
#     sl = a
#     a = c
#     c = sl
# if b > c:
#     sl = b
#     b = c
#     c = sl
# print "a = %d,b = %d,c = %d"%(a,b,c)


#   ******************if elif else 的用法*************************
# d = input()
#
# if d > 0:
#     print "d > 0"
# elif d == 0:
#     print "d = 0"
# else:
#     print "d < 0"

#   *************************学生成绩********************************
f = input()

if f >= 90:
    print "成绩为A"
elif 80 <= f < 90:
    print "成绩为B"
elif 70 <= f < 80:
    print "成绩为C"
elif 60 <= f < 70:
    print "成绩为D"
elif f < 60:
    print "成绩不及格"
