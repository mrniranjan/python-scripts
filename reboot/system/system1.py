#!/usr/bin/env python
import sys 
import time

s1 = sys.platform
current_time = time.clock
unix_time = time.time
#timeReceived = unix_time()
timeReceived = time.time()
print current_time()
print timeReceived

print s1

