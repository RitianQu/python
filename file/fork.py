#!/usr/bin/python

import os,time
pid = os.fork()
if pid < 0:
    print 'error'
elif pid == 0:
    print 'child',os.getpid()
    print os.getppid()
else:
    time.sleep(0.1)
    print os.waitpid(-1,os.WNOHANG)
    print 'parent',os.getpid()
    print pid
    while True:
        pass
print '========================='
