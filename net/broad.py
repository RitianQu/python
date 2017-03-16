#!/usr/bin/python
# coding=utf-8

import socket,sys
from time import sleep

dest = ('<broadcast>',9999)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
print '你瞅啥'

while True:
    sleep(1)
    s.sendto('hello',dest)
    buf,address = s.recvfrom(2048)
    if not len(buf):
        break
    print 'received from %s:%s'%(address,buf)
