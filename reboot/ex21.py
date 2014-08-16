def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "Multiplication %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "Divide %d by %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age : %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyway.
print "Here is the puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"


# Normal flow 

p = divide(iq, 2) 
print "output from divide function: %d" % p

q = multiply(weight, p)
print "output from multiply function: %d" % q

r = subtract(height, q)
print "output from subtract function: %d" % r

s = add(age, r)
print "output from add function: %d" % s


# This is what is happening

out = ( 30 + ( 78 - (90 * (100 / 2))))

print "output = %d" % out


# Reverse 

what = divide(iq, multiply(weight, subtract(height, add(age, 5))))

print "That becomes:", what, "Can you do it by hand?"
