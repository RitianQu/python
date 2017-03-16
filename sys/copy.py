#!/usr/bin/python
# coding=utf-8

import sys,os


try:
    fd_src = open(sys.argv[1],'r+')
except:
    print "open fd_src failed"

fd_src.seek(0,2)#光标位置定位到最后
size = fd_src.tell()#size等于第一个文件有多少字节


try:
    fd_dst = open(sys.argv[2],'w+')
except:
    print "open fd_dst failed"

size /= 2

pid = os.fork()#创建进程

if pid < 0:#os.fork()返回值如果小于0，则创建失败
    print "fail to fork"
    exit(-1)
elif pid == 0:#os.fork()返回值如果为零，则执行子进程
    fd_src.close()
    fd_dst.close()
    fd_src = open(sys.argv[1],'r+')
    fd_dst = open(sys.argv[2],'w+')

    fd_src.seek(size,0)#光标停在size处
    fd_dst.seek(size,0)

    while True:
        buf = fd_src.readline()
        if buf == '':#buf为空时，已读完下半部分
            break
        fd_dst.write(buf)#写入下半部分到第二个参数文件中

    exit(0)
else:
    num = 0
    fd_src.seek(0,0)
    fd_dst.seek(0,0)
    while True:
        buf = fd_src.readline()

        if num <= size:
            fd_dst.write(buf)
        else:
            break
        num += len(buf)

    os.wait()
    exit(0)
