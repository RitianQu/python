#!/usr/bin/python

f = lambda x,y,z:x+y+z
print f(2,3,4)


l = [lambda x:x ** 2,
     lambda x:x ** 3,
     lambda x:x ** 4]

for a in l:
    print a(2)
