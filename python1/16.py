#!/usr/bin/python


def fun(a,b):
    sum = 0
    d = len(b)
    for i in b:
        if i == a:
            sum += 1
    return sum


c = fun('l','hello world')
print c
