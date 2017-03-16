#!/usr/bin/python
import os,sys,time

f = open('test.txt','r')
f_new = open(sys.argv[1],'w+')
b = os.stat('test.txt')

c = b.st_size
d = c / 2
e = f.read(d)
g = f.read(18 - d)
a = os.fork()

if a < 0:
    print 'error'
elif a > 0:
    f_new.write(e)
else:
    time.sleep(0.1)
    f_new.write(g)
