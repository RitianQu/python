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
    buf = f.readline()
    print buf
    s = sys.stdin.readline()
    f.write(s)
    f.flush()
