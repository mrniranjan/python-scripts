## This program check if sum of two odd numbers and 1 even number is even

def sum(n1):
	sum = 0
	count = 0
	
	for i in n1:
		sum += n1[count]
		count += 1

	if (sum % 2) == 0:
		return True
	else:
		return False

numbers = []
for i in range(1, 4):
	data = raw_input("Enter Number:")
	data = int(data)
	numbers.append(data)

if sum(numbers):
	print "Sum of %r is Even" % numbers
else:
	print "Sum of %r is odd" % numbers
	
