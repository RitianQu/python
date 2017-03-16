#!/usr/bin/python
# coding=utf-8

import multiprocessing
import time

def wait_for_event(e):
    '''Waiting for the event to be set befor doing anything'''
    print 'wait_for_event : starting'
    e.wait()#等待事件
    print 'wait_for_event:e.is_set()->',e.is_set()

def wait_for_event_timeout(e,t):
    '''wait seconds and then timeout'''
    print 'wait_for_event_timeout : starting'
    e.wait(t)#等待两秒，不传入信号将开启
    print 'wait_for_event_timeout : e.is_set()->',e.is_set()

if __name__ == '__main__':
    e = multiprocessing.Event()#事件
    w1 = multiprocessing.Process(name = 'block',target = wait_for_event,args = (e,))#创建进程args以元组的形式传参给e


    w1.start()#开启进程

    w2 = multiprocessing.Process(name = 'non-block',target = wait_for_event_timeout,args = (e,2))

    w2.start()

    print 'main : waiting before calling Event.set()'
    time.sleep(4)
    e.set()#打开事件
    print 'main : event is set'
