#!/usr/bin/python3
#coding=utf-8
#  *******************while　循环*************************
# i = 1
# s = 1
#
# while i < 10:
#     s = (s + 1) * 2
#     i += 1
#
# print "桃子总数为%d"%s


# ********************for 循环**********************
# for i in [1,2,3,4,5]:
#     print "列表%d"%i
# print ""
#
# for i in (1,2,3,4,5):
#     print "元组%d"%i
# print ""
#
# for i in {1,2,3,4,5}:
#     print "集合%d"%i
# print ""
#
# for i in {"a":1,"b":2,"c":3}:
#     print "字典的键%s"%i
# print ""
#
# for i in "hello":
#     print "字符串%s"%i
# print ""

# ****************for　循环两个数***********************
# for (i,j) in [(1,2),(3,4),(5,6)]:
#     print i,j

# *********************九九乘法表****************************
i = 1
j = 1
for i in range(1,10):
    for j in range(1,i + 1):
        print "i * j = %d  "%(i*j),
    print ""


#****斐波那契数列,从第三个数开始，每个数都是前两个数的和************
# l = [1,1]
# for i in range(10):
#     n = l[i] + l[i+1]
#     l.append(n)
# print l

#********水仙花数**********
# for i in range(100,1000):
#     a = i / 100
#     b = i / 10 % 10
#     c = i % 10
#     if i == a ** 3 + b ** 3 + c ** 3:
#         print "%d"%i,
# print ""

#****************质数************************
# flag = 0
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j == 0:
#             flag = 0
#             break
#         else:
#             flag = 1
#     if flag == 1:
#         print "%d "%i

# ***************完数**********************
# s = 0
# for i in range(2,1000):
#     for j in range(1,i):
#         if i % j == 0:
#             s += j
#     if s == i:
#         print s
#     s = 0
# print ""

# ****************break continue***********************
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         # break        #只打印出1,2,3,4
#         continue    #打印出1,2,3,4,6,7,8,9,10,没有5
#     print i
# else:
#     print "+++++++++++++++++++++"

# *****************zip 生成字典******************************
# keys = ['a','b','c']
# vals = [1,2,3]
# print list(zip(keys,vals))     #[('a',1),('b',2),('c',3)]
#
# d = {}
# for (i,j) in zip(keys,vals):
#     d[i] = j
# print d
