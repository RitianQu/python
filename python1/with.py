#!/usr/bin/python
#coding=utf-8
class Test(object):
    def __del__(self):
        print "del...."

    def __enter__(self):
        print "enter...."

    def __exit__(self,type,value,traceback):
        print "exit...."



with Test() as Thing:#使用时先运行enter结束时运行exit，结束自动销毁对象
    print "doing something"

print "over"
