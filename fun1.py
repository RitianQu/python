#!/usr/bin/python

def func(a,b):
	a += 1
	b += 1
	print a,b
	print id(a),id(b)

#func(1,2)

x,y = 5,6
print id(x),id(y)
func(x,y)
