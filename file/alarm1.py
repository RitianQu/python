#!/usr/bin/python

import signal
import time

signal.alarm(6)

time.sleep(3)

num = signal.alarm(5)
print num
while True:
    time.sleep(1)
    print "==========="
