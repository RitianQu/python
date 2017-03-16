#!/usr/bin/python
#coding=utf-8

from socket import *
from time import sleep
import sys
import os
'''
实现FTP服务器的功能：
'''
#服务器功能函数
class FtpServer(object):
    BUFSIZE = 1024
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        filelist = os.listdir('.')#返回当前目录下所有文件

        if filelist == None:
            self.connfd.send('FAIL')#如果filelist为空　向客户端发送一个FAIL
            return

        self.connfd.send('OK')#如果不为空　向客户端发送一个OK
        sleep(0.01)

        for filename in filelist:#遍历filelist
            if filename[0] != '.' and os.path.isfile(filename):#判断filelist的每一项　不要.开头的　和　只要文件
                self.connfd.send(filename)#发送文件名
                sleep(0.01)#睡眠0.01秒　
        print "list OK !"
        sleep(0.01)
        return

    def do_get(self,filename):
        try:
            fd = open(filename,'rb')
        except:
            self.connfd.send('FAIL')

        self.connfd.send('OK')
	    sleep(0.01)

        while True:
            data = fd.readline()
            if not data:
                break
            self.connfd.send(data)
            sleep(0.01)

        fd.close()
        print "get OK"
        return

    def do_put(self,filename):
        try:
            fd = open(filename,'wb')
        except:
            self.connfd.send('FAIL')

        self.connfd.send('OK')

        while True:
            data = self.connfd.recv(self.BUFSIZE)
            if not data:
                break
            fd.write(data)

        fd.close()
        print "put OK"
        return



#创建套接字等工作
def main():
    if len(sys.argv) < 3:
        print "Input valid arg"
        sys.exit(0)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    BUFSIZE = 1024

    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)

    while True:
        connfd,addr = sockfd.accept()
        print "Connected from:",addr

        data = connfd.recv(BUFSIZE)
        ftp = FtpServer(connfd)

        print ">>>>",data

        if data[0] == 'L':
            ftp.do_list()

        if data[0] == 'G':
            ftp.do_get(data[2:])

        if data[0] == 'P':
            ftp.do_put(data[2:])

        connfd.close()


if __name__ == '__main__':
    main()
