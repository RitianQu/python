#!/usr/bin/python

a = raw_input()
b = len(a)
s = 0
for x in a:
    c = int(x)
    d = c * (10 ** (b-1))
    b -= 1
    s += d
print "%d"%s
