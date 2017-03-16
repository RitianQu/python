#!/usr/bin/python
# coding=utf-8

from multiprocessing import Pool
import os,time,random


def test(name):#建立函数
    print "start....."
    time.sleep(2)
    print "Task %s is run....."%name
    print "end...."



if __name__ == '__main__':
    print "parent pid : ",os.getpid()#获得pid
    p = Pool(4)#最多能同时进行4个子进程

    for i in range(5):
        p.apply_async(test,args = (i,))#向p中加入子进程，默认函数为子进程，整个文件为父进程，共调用5次子程序

    p.close()
    p.join()#阻塞模式，当p中所有子进程结束时通过阻塞

    print "All processs end"
