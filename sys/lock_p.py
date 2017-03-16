#!/usr/bin/python
# coding=utf-8

import multiprocessing
import sys
from time import sleep


def worker_with(lock,stream):
    with lock:#上琐
        for i in range(5):
            sleep(1)
            stream.write('Lock acquired via with\n')
#执行结束自动解锁
def worker_no_with(lock,stream):
    lock.acquire()#上琐
    try:
        for i in range(5):
            sleep(1)
            stream.write('Lock acquired directly\n')
    finally:
        lock.release()#解锁

lock = multiprocessing.Lock()#琐
w = multiprocessing.Process(target = worker_with,args = (lock,sys.stdout))
#创建一个进程
nw = multiprocessing.Process(target = worker_no_with,args = (lock,sys.stdout))
#创建一个进程
w.start()
nw.start()

w.join()
nw.join()
