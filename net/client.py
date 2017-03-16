#!/usr/bin/python

from socket import *
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFSIZE = 1024

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(ADDR)

while True:
    data = raw_input()
    sockfd.send(data)
    data = sockfd.recv(BUFSIZE)
    print data
    if data == 'quit':
        exit()
    else:
        break
while True:
    data = raw_input()
    sockfd.send(data)
    data = data.split(' ')
    data1 = data[1]
    sockfd.recv(BUFSIZE)
    if data == 'buf':
        f = open('data1','a+')
        a = sockfd.recv(BUFSIZE)
        f.write(a)
