#coding=utf-8

def fun():
#    a = 3
#    b = 4
    global a #声明全局变量
    a += 1
    print "in fun:",a,b
    num = 1000


a = 1
b = 2
fun()
print "out fun:",a,b
#print num
