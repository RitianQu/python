#!/usr/bin/python
import sys

f = open(sys.argv[1],'a+')

while True:
    a = sys.stdin.readline()
    if a == '#\n':
        break
    f.write(a)
f.close()
