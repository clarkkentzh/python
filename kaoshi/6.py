#coding=utf-8

import math

st = raw_input()
lists = st.split(" ")
rows = int(math.sqrt(len(lists)))

k = 0
list1 = []
list2 = []
for i in range(rows):
    list1.append([])
    for j in range(rows):
        list1[i].append(lists[k])
        k += 1

def fun1(lists):
    for i in lists[0]:
        list2.append(i)
    del lists[0]
    return lists
def fun(lists):
    a = fun1(lists)
    b = map(list,zip(*a))
    b.reverse()
    if(len(b) >= 1):
        fun(b)
fun(list1)
print list2
