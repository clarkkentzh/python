#coding=utf-8

a = input()

# assert后的判断不符合时抛出AssertionError错误
try:
    assert a > 5
    if a > 5:
        print "a > 5"
    else:
        print "a < 5"
except AssertionError:
    print "错误了"
