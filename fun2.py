#!/usr/bin/python

def fun(l):
	l[3] = 100
	print "fun:",l

def fun1(a):
	a = 100
	print "fun:",a

l = [1,2,3,4,5]

fun(l)

print "main:",l


a = 2

fun1(a)

print "main:",a
