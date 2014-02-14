#!/usr/bin/python
def print_two(*args):
	arg1,arg2,arg3 = args
	print "arg1: %r, arg2: %r,arg3: %r" % (arg1,arg2,arg3)

""" ok, that *args actually pointless, we can just do this """

def print_two_again(arg1,arg2):
	print "arg1: %r, arg2 %r" % (arg1,arg2)

def print_one(arg1):
	print "arg1: %r"  % arg1

def print_none():
	print "I got nothin."

print_two("Zed","Shaw","hello")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()



