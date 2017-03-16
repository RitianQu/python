#!/usr/bin/python
# coding=utf-8

import os,time


pid = os.fork()#创建进程

if pid < 0:#如果os.fork()返回值小于0则创建失败
    print "create process error"
elif pid == 0:#如果os.fork()返回值等于0则为子进程
    pid = os.fork()#创建进程

    if pid < 0:#如果os.fork()返回值小于0则创建失败
        print "create process error"
    elif pid == 0:#如果os.fork()返回值等于0则为子进程
        while True:
            time.sleep(1)
            print "greatson do something"
    else:#父进程结束，子进程被init继养，消除子进程的尸体，防止僵尸进程
        exit()
else:
    os.wait()#阻塞模式，系统中任意子进程结束捕捉
    while True:
        time.sleep(1)
        print "parent do something"
