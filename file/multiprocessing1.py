#!/usr/bin/python

import multiprocessing

from time import ctime,sleep

import os

def worker(interval = 2):
    n = 5

    while n > 0:
        print 'the time is {}'.format(ctime())
        print 'worker pid >>',os.getppid()
        sleep(interval)
        n -= 1

def teacher(interval = 2):
    n = 5

    while n > 0:
        print 'the time is {}'.format(ctime())
        print 'teacher pid >>',os.getppid()
        sleep(interval)
        n -= 1

if __name__ == '__main__':
    p = multiprocessing.Process(name = 'worker',target = worker)
    p.start()
    q = multiprocessing.Process(name = 'teacher',target = worker)
    q.start()

    p.join()
    q.join()

    print 'p.pid:',p.pid
    print 'p.name',p.name
    print 'p.is_alive:',p.is_alive
    print 'q.pid:',q.pid
    print 'q.name',q.name
    print 'q.is_alive:',q.is_alive
