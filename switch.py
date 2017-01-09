#!/usr/bin/python

x = input()
o = raw_input()
y = input()
def jia(x,y):
    print x+y

def jian(x,y):
    print x-y

def cheng(x,y):
    print x*y

def chu(x,y):
    print x/y

operator = {'+':jia,'-':jian,'*':cheng,'/':chu}

def f(x,o,y):
    operator.get(o)(x,y)


f(x,o,y)
