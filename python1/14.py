#!/usr/bin/python

'''
def func():
    print"hello world!"
print "++++++++++++++++"
func()
f = func

f()

def fun(a , b):
    return a + b
print fun(1,2)
a = fun(1,2)
print a
'''
def fun(a):
    a.append(5)
    print a
l = [1,2,3,4]
a = l[:]
fun(a)
print l
def fun1(a,b):
    print a,b
def fun2(a,b=10,*c,**d):
    print a,b,c,d
fun2(1,2,3,4,5,e = 1,f = 2)
