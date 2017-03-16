#!/usr/bin/python
# coding=utf-8

import MySQLdb

db = MySQLdb.connect('localhost','root','1','testdb')#生成操作数据库的对象

cursor = db.cursor()#生成操作内容的对象
try:
    cursor.execute('select * from newtab')

    data = cursor.fetchall()

    print 'get data',data

    for i in cursor.description:
        print i[0],

    print ''


    for com in data:
        firstname = com[0]
        lastname = com[1]
        age = com[2]
        sex = com[3]
        num = com[4]

        print 'firstname:{0},lastname:{1},age:{2},sex:{3},num:{4}'.format(firstname,lastname,age,sex,num)

except:
    print 'Error:unable to fecth data'
db.close()
