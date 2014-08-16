# Get all the numbers which are prime and composite between 1 and 20
def prime_number(n1):
	result = []
	for i in n1:
		temp = 0
		count = 2
		#print "i = %d" % i
		val = i // 2
		#print "val = %d" % val
		while count <= val:
			temp = i % count
			#print "temp = %d" % temp
			if temp == 0:
				break
			else:
				count += 1
		if temp != 0:
			result.append(i)
	return result

def composite_numbers(n1):
	factors = []
	for i in n1:
		count = 1
		check = 0
		while count <= i:
			temp = i % count
			if temp == 0:
				check += 1
			count += 1
		if check > 2:
			factors.append(i)
	return factors		


n1 = []
lower = 1
upper = 21
print "Please enter 20 numbers"
for i in range(lower, upper):
	data = raw_input("Enter number:")
	data = int(data)
	n1.append(data)

print "Prime numbes between %d and %d are: %r" % (lower, upper-1, prime_number(n1))
print "Composite Numbers between %d and %d are: %r" % (lower, upper-1, composite_numbers(n1))



	 
