#!/usr/bin/python
# coding=utf-8

import socket,traceback

HOST = ''
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((HOST,PORT))

while True:
    try:
        message,address = s.recvfrom(4096)
        print 'got data from',address
        s.sendto('你瞅啥',address)
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
