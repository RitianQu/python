#!/usr/bin/python

from time import sleep
import os,sys

try:
    os.mkfifo('fifo')
except OSError:
    print 'fifo exist'

f = open('fifo','a+')

while True:
    #sleep(1)


    f.write(sys.stdin.readline())
    f.flush()
    buf = f.readline()
    print buf
