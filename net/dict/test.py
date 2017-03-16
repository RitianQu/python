#!usr/bin/python

def a():
    name = 'abc'
    c(name)

def c(name):
    b(name)

def b(name):
    print name

a()
