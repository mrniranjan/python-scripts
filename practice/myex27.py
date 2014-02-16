def square(arg1):
	value = arg1 * arg1
	print "\nSquare of %d is %d" % (arg1,value)
a = 10
square(10)
square(10 + 10)
square((3*5)+(9*10))
square(a+10 * a - 10)
a = raw_input("Enter a number:")
square(int(a))
