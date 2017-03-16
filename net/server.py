#!/usr/bin/python

from socket import *
import sys,os

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFSIZE = 1024

sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

connfd,addr = sockfd.accept()

while True:
    data = connfd.recv(BUFSIZE)
    data = data.split(' ')
    data = data[0]
    if data == 'list':
        a = os.listdir('.')
        connfd.send('[%s]\n'%a)
    elif data == 'quit':
        connfd.send('quit')
        exit()
    elif data == 'get':
        data1 = data[1]
        f = open('data1','r')
        buf = f.readline()
        connfd.send('buf')
        print buf
