from sys import argv
from os.path import exists

script, from_file = argv

def addition(*args):
	"""This function will add numbers"""
	arg1, arg2 = args
	sum = arg1 + arg2
	return sum

def multiply(*args):
	"""This function will multiply numbers"""
	arg1, arg2 = args
	mul = arg1 * arg2
	return mul

def division(*args):
	"""This function will divide numbers"""
	arg1, arg2 = args
	div = arg1/arg2
	return div



in_file = open(from_file, 'w')

print " Does the file exists? %r" % exists(from_file)
print " Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

s1 = "We will calculate mean of 2 numbers"

n1 = raw_input("Enter first number:")
n2 = raw_input("Enter second number:")

total = addition(int(n1), int(n2))
mean = division(total, 2)

s2 = "Mean of %s and %s is: %d" % (n1, n2, mean)

in_file.write(s2)
in_file.close()

in_file = open(from_file)
print in_file.read()

in_file.close()

