#!/usr/bin/python
# coding=utf-8

from time import ctime,sleep
import os,threading

def super_player(file,time):
    for i in range(1):
        print 'start playing: %s .%s'%(file,ctime())
        sleep(time)

l = {'Baby.mp3':3,'Anatar.mp4':5,'U and M':4}

threads = []
files = range(len(l))

for file,time in l.items():#迭代器items生成一个列表，列表中每项为一个元组，元组中分别为键和值，file为键，time为值
    t = threading.Thread(target = super_player,args=(file,time))
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print 'end %s'%ctime()
