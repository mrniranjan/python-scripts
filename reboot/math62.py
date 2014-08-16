# this program check if product of three odd numbers is odd
def product(n1):
	out = 1
	count = 0
	
	for i in n1:
		out *= n1[count]
		count += 1
	print out	
	if (out % 2) == 0:
		return True
	else:
		return False


numbers = []
for i in range(1, 4):
	data = raw_input("Enter Number:")
	data = int(data)
	numbers.append(data)

if product(numbers):
	print "Product of %r is Even" % numbers
else:
	print "Product of %r is odd" % numbers
		
