 #! /usr/bin/python

from time import ctime,sleep

def music():
    print('I was listening to music.%s'%ctime())
    sleep(2)

def move():
    print('I was at the movies! %s'%ctime())
    sleep(5)

music()
move()

print("all over %s"%ctime())

