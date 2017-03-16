#!/usr/bin/python
# coding=utf-8
#协程
import greenlet#需下载

def test1():
    print 12
    gr2.switch()#记录位置，当再次调用test1记录上次执行位置，继续执行下面语句
    print 34

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
gr1.switch()
