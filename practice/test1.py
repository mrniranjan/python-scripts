#!/usr/bin/python
def fun1(a):
	return abs(a)

def fun2(a):
	return ord(a)

#print "absolute value: %d" % fun1(float(raw_input("Enter a number:?")))
print "UTF 8 value is : %s" % fun2(raw_input("Enter a character: "))

