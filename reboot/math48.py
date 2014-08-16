def prime_number(number):
	temp = 0
	count = 2
	val = number // 2
	
	while count <= val:
		temp = number % count 
		if temp == 0:
			print "Number %d is not prime Number" % number
			return 0
		else:
			count += 1
	
	if temp != 0:
		print "Number %d is a Prime Number" % number

def factors(number):
	count = 1
	sum = 0
	while count <= number:
		temp = number % count
		if temp == 0:
			print "% d is a factor of %d" % (count, number)
			sum += count
		count += 1
	if sum == 2 * number: 
		print "Number %d is perfect number" % number
	else:
		print "Number %d is not a perfect Number" % number


number = raw_input("Enter a number: ")
number = int(number)

s1 = """
\t 1. Prime Number 
\t 2. Factors
"""

print s1 
choice = raw_input("Enter the operation to be performed:")

if int(choice) == 1:
	prime_number(number)
elif int(choice) == 2:
	factors(number)
else:
	print "Enter right choice"

