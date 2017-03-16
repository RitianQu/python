#!/usr/bin/python
#coding=utf-8

#用于线程间通信 通过事件标识控制

import threading
from time import sleep,ctime

e = threading.Event()#创建线程事件对象
def wait_for_event():
    '''wait for the event to be set before doing anything'''
    print('wait for event starting')
    event_is_set = e.wait()#阻塞
    print('event set1:%s'%event_is_set)

def wait_for_event_timeout(t):
    '''wait t seconds and then timeout'''
    while not e.isSet():#阻塞是否被设置
        print('wait for event timeout starting')
        event_is_set = e.wait(t)#阻塞t秒
        print('event set2:%s'%event_is_set)
        if event_is_set:#如果阻塞被设置，e.wait()为True，如果没有被设置返回值为False
            print('processing event')
        else:
            print('doing other work')

t1 = threading.Thread(name = 'block',target = wait_for_event,args = ())
t1.start()
t2 = threading.Thread(name = 'nonblock',target = wait_for_event_timeout,args =
        (3,))
t2.start()

print('waiting before calling event.set()')
sleep(4)
e.set()#开启阻塞
print('event is set')
