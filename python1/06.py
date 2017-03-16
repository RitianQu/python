#!/usr/bin/python
#coding=utf-8

d = {1:'石头',2:'剪刀',3:'布'}
import random
while True:
    s = raw_input()
    if s == d[1]:
        s = 1
    elif s == d[2]:
        s = 2
    elif s == d[3]:
        s = 3
    else:
        print '请输入 ： '
        continue
    a = random.randint(1,3)
    print "you：%s,robot：%s"%(d[s],d[a])
    if s == 1:
        if a == 1:
            print 'go on'
        elif a == 2:
            print 'you win'
        elif a == 3:
            print 'you lose'
    if s== 2:
        if a == 1:
            print 'you lose'
        elif a == 2:
            print 'go on'
        elif a == 3:
            print 'you win'
    if s == 3:
        if a == 1:
            print 'you win'
        elif a == 2:
            print 'you lose'
        elif a == 3:
            print 'go on'
