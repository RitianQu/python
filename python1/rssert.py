#!/usr/bin/python
#coding=utf-8
a = input()

try:
    assert a > 5#如果条件满足正常运行，不满足则被except捕捉
    if a > 5:
        print "a > 5"
    else:
        print "a < 5"
except AssertionError:
    print "NO assert error"
