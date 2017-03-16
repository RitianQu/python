#!/usr/bin/python
# coding=utf-8

import os,time

pid = os.fork()#创建进程

if pid < 0:#os.fork()返回值小于零则创建失败
    print "create process failed"
elif pid == 0:#os.fork()返回值等于零则为子进程
    print "This is child process",os.getpid()
    print os.getppid()
    exit('hahahha')

else:#os.fork()返回值大于零则为父进程
    time.sleep(0.1)#睡眠0.1S
    print os.waitpid(-1,os.WNOHANG)#阻塞模式
    print "This is parent process",os.getpid()
    print pid
    while True:
        pass

print "+++++++++++++++++++"
