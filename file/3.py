#!/usr/bin/python
import sys

f = open(sys.argv[1],'r')

f_cp = open(sys.argv[2],'w')

while True:
    a = f.readline()
    if a == '':
        break
    f_cp.write(a)
