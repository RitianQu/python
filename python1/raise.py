#!/usr/bin/python

class ShortInputError(Exception):
    def __init__(self,length,least):
        super(ShortInputError,self).__init__(self)
        self.length = length
        self.least = least

try:
    s = raw_input("Input >>")
    if len(s) < 3:
        raise ShortInputError(len(s),s)

except EOFError:
    print "Input EOF"
except ShortInputError as x:
    print "ShortInputError:your input %s,at least %s"%(x.length,x.least)
else:
    print "No error"
