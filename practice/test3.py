#!/usr/bin/python
import os

def myfunc(input_string, timeout=2,count=4):
	print input_string
	print timeout
	print count

myfunc("Hi","HI","ABC")
my_id = os.getpid() & 0xFFFF
my_id2 = os.getpid()
print my_id
print my_id2
