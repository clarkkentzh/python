#coding=utf-8


class Father(object):
    def __init__(self,num):
        self.num = num
    def maopao(self,lists):
        for i in range(self.num):
            for j in range(i):
                if lists[j] > lists[j + 1]:
                    lists[j],lists[j + 1] = lists[j + 1],lists[j]
        return lists
    def xuanze(self,lists):
        for i in range(self.num):
            small = i
            for j in range(i + 1,self.num):
                if lists[small] > lists[j]:
                    small = j
            datas = lists[small]
            lists[small] = lists[i]
            lists[i] = datas
        return lists

class Son(Father):
    def __init__(self,num):
        self.num = num
    def kuaisu(self,lists,left,right):
        i = left
        j = right
        if (i >= right):
            return lists
        key = lists[i]
        while i < j:
            while i < j and lists[j] >= key:
                j -= 1
            lists[i] = lists[j]
            lists[j] = key
            while i < j and lists[i] <= key:
                i += 1
            lists[j] = lists[i]
            lists[i] = key
        print "*****",lists
        self.kuaisu(lists,left,i - 1)
        self.kuaisu(lists,j + 1,right)
        return lists

l = [5,3,4,65,9]
a = Father(len(l))
# print a.maopao(l)
# print a.xuanze(l)

l1 = [8,6,7,89,10]
b = Son(len(l1))
print b.kuaisu(l1,0,len(l1)-1)
