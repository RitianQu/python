#!usr/bin/python
#coding=utf-8

a=raw_input("请按照以下格式输入日期“2008-1-2”:")
l=a.split("-")#令l=以“-”为断点的列表
year=int(l[0])
mon=int(l[1])
data=int(l[2])#year，mon，data为整数型
yearflag=0#yearflag=0为年标识位
monflag=0#monflag=0为月标识位
dic1={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#定义一个年为闰年的字典，key为月份，value为天数
dic2={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#定义一个年尾平年的字典，key为月份，value为天数
result=0
if year<0 or mon < 0 or mon > 12 or data < 0 or data > 31:#判断输入是否有错误
    print "erro!"
    exit()
if year % 400 ==0 or year % 4 == 0 and  year % 100 != 0:#判断年是否为闰年
    yearflag=1#年为闰年，则yearflag=1
    print "runnian"
if mon in [1,3,5,7,8,12]:#判断输入月份是否在这些月份中
    pass
elif mon == 2 :
    monflag=2#如果输入月份为2月，则monflag=2
else:
    monflag=1
if monflag == 1 and data > 30:#判断月份是否为小月，是否大于30天
    print "小月的天数最多有30天"
    exit()
if yearflag==1 and monflag==2 and data > 29 :#判断是否为闰年的二月份，是否大于29天
    print "闰年的2月最多有29天"
    exit()
if yearflag == 0 and monflag == 2    and data > 28 :#判断是否为平年的二月份，是否大于28天
    print "平年的2月最多有28天"
    exit()
if yearflag==1:#如果是闰年
    for i in range(1,mon):#从1到输入的月份开始循环
        result+=dic1[i]
        print result
if yearflag==0:
    for i in range(1,mon):
        result+=dic2[i]
        print result
result+=data
print result
print "%s是%d年的第%d天"%(a,year,result)
