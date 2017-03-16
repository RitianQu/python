#!/usr/bin/python
import time
z = 0
try:
    f = open('file.py','a+',0)
except IOError,e:
    print e

for i in f:
    z += 1
while True:
    z += 1
    a = time.localtime()
    print >>f,'%d, %d-%d-%d %d:%d:%d'%(z,a.tm_year,a.tm_mon,\
    a.tm_mday,a.tm_hour,a.tm_min,a.tm_sec)
    time.sleep(1)
