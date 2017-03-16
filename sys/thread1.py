#! /usr/bin/python
# coding=utf-8

from time import ctime,sleep
import threading

def music(name):
    print('I was listening to music %s .%s'%(name,ctime()))
    sleep(2)

def move(name):
    print('I was at the movie %s! %s'%(name,ctime()))
    sleep(5)

threads =[]

t1 = threading.Thread(target = music,args = ('baby',))
t2 = threading.Thread(target = move,args = ('afanda',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        t.setDaemon(True)#加setDaemon主线程结束，则程序结束，不加上如果主线程结束，会随机挑选一个线程成为主线程
        t.start()
    t.join()

    print("all over %s"%ctime())
