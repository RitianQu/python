#!/usr/bin/python

a = 5

def fun():
    global a
    a += 1

fun()
print(a)
