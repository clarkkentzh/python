#coding=utf-8

class Node(object):
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class Linklist(object):
    def __init__(self):
        self.head = None

    def startlist(self,data):
        self.head = Node(0)

        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

    def show(self):
        p = self.head.next

        while p != None:
            print p.val
            p = p.next

    def getlength(self):
        p = self.head

        lens = 0
        while p.next != None:
            lens += 1
            p = p.next
        return lens

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def inserts(self,index,datas):
        if self.is_empty() or index > self.getlength() or index < 0:
            print "出错了"
            return
        p = self.head
        j = 0

        while p.next != None and j < index:
            p = p.next
            j += 1

        q = Node(datas)
        q.next = p.next
        p.next = q

    def deletes(self,index):
        if self.is_empty() or index > self.getlength() or index < 0:
            print "出错了"
            return

        p = self.head
        j = 0

        while p.next != None and j < index:
            p = p.next
            j += 1

        if p.next == None:
            print "index is error!"
        else:
            p.next = p.next.next

    def finds(self,value):
        if self.is_empty():
            print "空的"
            return
        p = self.head
        i = 0
        while p.next != None and p.val != value:
            p = p.next
            i += 1
        if p.next == None:
            return -1
        else:
            return i

    def adds(self,shu):
        if self.is_empty() and shu.is_empty():
            return
        p1 = self.head
        p2 = shu.head
        l1 = []
        l2 = []
        l3 = []
        while p1.next != None:
            p1 = p1.next
            l1.append(p1.val)
        while p2.next != None:
            p2 = p2.next
            l2.append(p2.val)
        lens = len(l2) if len(l1) >= len(l2) else len(l1)
        lens1 = l1 if len(l1) > len(l2) else l2

        for i in range(lens):
            if l1[i] + l2[i] < 10:
                if len(l3) == i + 1:
                    l3[i] = l1[i] + l2[i] + l3[i]
                else:
                    l3.append(l1[i] + l2[i])
            else:
                l3.append((l1[i] + l2[i]) % 10)
                l3.append((l1[i] + l2[i]) / 10)
        for i in range(lens,len(lens1)):
            if lens1[i] < 10:
                 if len(l3) == i + 1:
                     l3[i] = lens1[i] + l3[i]
                 else:
                     l3.append(lens1[i])
            else:
                l3.append(lens1[i] % 10)
                l3.append(lens1[i] / 10)
        return l3
# zhao = Linklist()
# zhao.startlist([1,2,3,4,5,6])
# zhao.show()
# zhao.inserts(2,50)
# zhao.show()
# print zhao.finds(36)    # 找不到返回-1
# print zhao.finds(50)    # 找到返回1
# # 删除是靠后删，即删除索引值后面的数据
# zhao.deletes(1)
# print "+++++++++++++++++++++++"
# zhao.show()
print "-------------------------------------------------------------------"
s1 = Linklist()
s2 = Linklist()
s1.startlist([1,2,3,4])
s2.startlist([5,6,7])
print s2.adds(s1)
