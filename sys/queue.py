#!/usr/bin/python
# coding=utf-8

from multiprocessing import Process,Queue

import time

process_list = []
q = Queue()

def f(name):
    time.sleep(1)
    q.put(['hello' + str(name)])#放入队列中

if __name__ == '__main__':
    for i in range(10):
        p = Process(target = f,args = (i,))
        p.start()
        process_list.append(p)
    for j in process_list:
        j.join()
    for i in range(10):
        print q.get()[0]#从队列中取出
