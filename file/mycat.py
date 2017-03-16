#!/usr/bin/python
import sys

try:
    f = open(sys.argv[1],'r')
    buf = f.read()
except IOError as e:
    print e

print buf
