#!/usr/bin/python

import os,time

pid = os.fork()

if pid < 0:
    print 'process error'
elif pid == 0:
    pid = os.fork()

    if pid < 0:
        print 'process error'
    elif pid == 0:
        while True:
            time.sleep(1)
            print 'greadson do something'
    else:
        exit()
else:
    os.wait()
    while True:
        time.sleep(1)
        print 'parent do something'
