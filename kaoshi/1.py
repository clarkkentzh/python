#coding=utf-8

def addr(*t):
    try:
        if type(t[0]) == int:
            sums = 0
            for i in t:
                sums += i
        elif type(t[0]) == str:
            sums = ''
            for i in t:
                sums += i
    except Exception as e:
        print e
    return sums

print addr(20,10,30)
print addr("a",'b','c')
