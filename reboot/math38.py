from sys import argv

script, arg1 = argv

def successor(arg1):
	print "Successor of %s is %d:" % (arg1, int(arg1) + 1)
	print "Predecssor of %s is %d:" % (arg1, int(arg1) - 1)

successor(arg1)


