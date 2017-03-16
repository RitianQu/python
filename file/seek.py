#!/usr/bin/python
import sys

f = open('text.txt','r+')

str = f.read(5)
print str

print f.tell()

f.seek(5,1)

str = f.read(5)

print str
print f.tell()

f.seek(2)
print f.tell()
