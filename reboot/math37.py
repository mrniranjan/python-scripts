from sys import argv
script, arg1, arg2 = argv

def greater(*args):
	arg1, arg2 = args
	s1 = int(arg1) > int(arg2)
	s2 = int(arg2) > int(arg1)
	s3 = "is %r greater than %r: %r" 
	print s3 % (arg1, arg2, s1)
	print s3 % (arg2, arg1, s2)

greater(arg1,arg2)

	
