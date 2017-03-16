#!/usr/bin/python
# coding=utf-8

from signal import *
from time import sleep

alarm(3)

#signal(SIGALRM,SIG_DFL)#采用默认方式处理
signal(SIGINT,SIG_IGN)#忽略信号

while True:
    pass
