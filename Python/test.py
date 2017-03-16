#!/usr/bin/python
#coding=utf-8

import random

d = {0:"石头",1:"剪刀",2:"布"}

while True:
    s = raw_input()
    if s == d[0]:
        s = 0
        #print s
    elif s == d[1]:
        s = 1
        #print s
    elif s == d[2]:
        s = 2
        #print s
    else:
        print "sorry input error"
        continue
    a = random.randint(0,2)#随机选出三个数
    print "you:%s,robot:%s"%(d[s],d[a])

    if s == 0:
        if a == 1:
            print "you win"
        elif a == 2:
            print "you lost"
    if s == 1:
        if a == 2:
            print "you win"
        elif a == 0:
            print "you lost"
    if s == 2:
        if a == 0:
            print "you win"
        elif a == 1:
            print "you lost"
