print "We will do 3 * (5 + 6) / 10 - 2 + (6 * 3)"

def add(a, b):
	print "Add %d +  %d" % (a, b)
	return a + b

def multiply(a, b):
	print "Multiple %d * %d" % (a, b)
	return a * b

def divide(a,b):
	print "Divide %d / %d" % (a, b)
	return a / b

def subtract(a, b):
	print "Subtract %d - %d" % (a,b)
	return a - b


out1 = 3 * (5 + 6) / 10 - 2 + (6 * 3)

p = add(subtract(divide(multiply(3, add(5, 6)), 10), 2), multiply(6, 3))

print "chained function output = %d" % p 
print "Direct computation result = %d" % out1
