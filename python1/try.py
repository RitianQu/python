#!/usr/bin/python

def div(a,b):
    try:
        c = a / b
        print "c:",c

    except (ZeroDivisionError,TypeError):
        print "zero can not be division"
    except:
        pass
    else:
        print "else....."
    finally:
        print "finally...."
    return c

result = div(3,0)

print result
print "test over"
