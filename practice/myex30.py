#!/usr/bin/python
#this program implments forumla 2 * b * y / (d + 1) - x / 3 * ( z + y)
def add(x,y):
	return x + y
def sub(x,y):
	return x - y
def mul(x,y):
	return x * y
def div(x,y):
	return x / y


def myformula(x,y,z,b,d):
	return (sub(div(mul(mul(2,b),y),add(d,1)),div(x,mul(3,add(z,y)))))


x = 3
y = 2
z = 1 
b = 7
d = 6

print """
This program implements formula 2 * b * y / (d + 1) - x / 3 * ( z + y) 
is %d when x = %d, y = %d, z = %d, b = %d, d = %d
""" % (myformula(3,2,1,7,6),x,y,z,b,d)

