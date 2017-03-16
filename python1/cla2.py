#!/usr/bin/python
#coding=utf-8
class Person(object):
    print "class....."

    def __new__(cls):#构造函数
        print "new....."
        return object.__new__(cls)

    def __init__(self):#初始化
        print "init....."

    def color(self):
        print "color....."

    def __del__(self):
        print "del....."

Lilei = Person()
Lilei.color()

del Lilei

Hanmei = Person()
Hanmei.color()
