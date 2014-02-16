#!/usr/bin/python
from sys import argv
script, x = argv

def add(a,b):
	return a + b
def mul(a,b):
	return a * b
def div(a,b):
	return a / b
def sub(a,b):
	return a - b
def square(a):
	return a * a

print "Answer for 3x^2 + 2x - 5  is: %d where x = %d " % (sub(add(2,mul(3,square(int(x)))),3),int(x))
