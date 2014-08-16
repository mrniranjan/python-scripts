def greater(*args):
	arg1, arg2 = args
	s1 = int(arg1) == int(arg2)
	print "checking if %r and %r ars are equal and they are : %r" % (arg1, arg2, s1)

def sum(*args):
	arg1, arg2 = args
	s1 = arg1 + arg2
	print "Sum of %d and %d is %d" % (arg1, arg2, s1)

def string(arg1):
	s1 = arg1
	print "hello" + " " + s1 
	
greater(25,25)
sum(25,25)
string("Pavan")

