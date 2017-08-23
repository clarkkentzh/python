#coding=utf-8
import time

line = 0
# while True:
#     time.sleep(1)
#     line += 1
#     fd = open("time.txt","a+")
#     s = time.localtime()
#     str = "%d,%4d-%02d-%02d %02d:%02d:%02d\n"%(line,s.tm_year,s.tm_mon,s.tm_mday,s.tm_hour,s.tm_min,s.tm_sec)
#     fd.write(str)
#     fd.close()


# ************标准代码＊＊＊＊＊＊＊＊＊＊

try:
    fd = open("time.txt","a+")
except IOError as e:
    print e

for i in fd:
    line += 1

while True:
    s = time.localtime()
    line += 1
    str = "%d,%4d-%02d-%02d %02d:%02d:%02d\n"%(line,s.tm_year,s.tm_mon,s.tm_mday,s.tm_hour,s.tm_min,s.tm_sec)
    fd.write(str)
    fd.flush()
    time.sleep(1)
