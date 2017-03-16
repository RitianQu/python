#!/usr/bin/python
#coding=utf-8
import traceback #引入异常错误行

def div(a,b):
    try:
        return a / b
    except (ZeroDivisionError,TypeError) as e:
        print e#打印异常原因
        traceback.print_exc()#异常错误分析
    else:
        print "else....."
    finally:
        print "finally...."

result = div(3,"c")

print result
print "test over"
