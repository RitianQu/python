#!/usr/bin/python

import smtplib
from smtplib import SMTP as smtp
import getpass

mail_host = 'smtp.163.com'
mail_user = '18722692210@163.com'
mail_pass = getpass.getpass()

sender = '18722692210@163.com'
receiver = ['lncyby@126.com']

message = '''From:18722692210@163.com\r\nTo:lncyby@163.com\r\nSubject:testmsg\r\n\r\nPython test email'''

print message

try:
    smtpobj = smtp(mail_host)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receiver,message)
    print 'ok'
except smtplib.SMTPException,e:
    print 'error:',e
