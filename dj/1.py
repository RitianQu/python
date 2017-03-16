#!/usr/bin/python

from ftplib import FTP
import sys.getpass,os.path

host,username,localfile,remotepath = sys.argv[1:]

password = getpass.getpass("Enter password for %s on %s:"%(username,host))
f = FTP(host)
f.login(username,password)
print remotepath
f.cwd(remotepath)
print f.dir()
print localfile
fd = open(localfile,'rb')
f.storbinary('STOP test',fd)
fd.close()
f.quit()
