#!/usr/bin/python

import ftplib,os,socket

host = 'ftp.kernel.org'
dirn = 'pub/linux/kernel'
FILE = 'README'
def main():
    f = ftplib.FTP(host)
    f.login()
    f.cwd(dirn)
    f.retrbinary("RETR %s"%FILE,open(FILE,'wb').write)
    f.quit()

if __name__ == '__main__':
    main()
