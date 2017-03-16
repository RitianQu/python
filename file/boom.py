#!/usr/bin/python

from signal import *
import time,os,multiprocessing

def son(signum,stack):
    if signum == SIGINT:
        print '++++++++++++'
        os.kill(a,SIGUSR1)

def parent(signum,stack):
    if signum == SIGUSR1:
        print "let's gogogo"



p = multiprocessing.Process(name = 'son')
p.start()
a = os.getppid()
signal(SIGINT,son)
signal(SIGUSR1,parent)
