#!/usr/bin/python

import multiprocessing
import time

def wait_for_event(e):
    print 'wait_for_event:starting'
    e.wait()
    print 'wait_for_event:e.is_set()->',e.is_set()

if __name__ = '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name = 'block',target = wait_for_event,args)
