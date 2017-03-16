#!/usr/bin/python
import os,time
pid = os.fork()
a = 0

if pid < 0:
        print "error"
elif pid == 0:
    while True:
        time.sleep(0.8)
        print "son"
        print a
else:
    while True:
        time.sleep(1)
        print "parent"
        print a
