#!/usr/bin/python

from socket import *
from time import ctime,sleep
import sys,os

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFSIZE = 1024

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(ADDR)
d = {}


def name():

    for i,j in d.items():
        if j == addr:
            pass
        else:
            sockfd.sendto(data,j)
while True:
    data,addr = sockfd.recvfrom(BUFSIZE)
    pid = os.fork()
    if pid:
        d[data] = addr
        print d
        continue
    else:
        sleep(0.1)
        while True:
            name()
            data,addr = sockfd.recvfrom(BUFSIZE)
            for i,j in d.items():
                if j == addr:
                    pass
                else:
                    sockfd.sendto(data,j)
