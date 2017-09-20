#! /usr/bin/python

from time import ctime,sleep
import threading

def music(func):
    print('Start playing: %s .%s'%(func,ctime()))
    sleep(2)

def move(func):
    print('Start playing: %s! %s'%(func,ctime()))
    sleep(5)

def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    else:
        print('error:The format is not recogzed')

l = ['Baby.mp3','Avatar.mp4']

threads =[]
files = range(len(l))

for i in files:
    t = threading.Thread(target = player,args = (l[i],))
    threads.append(t)

if __name__ == '__main__':

    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print ('end:%s'%ctime())

