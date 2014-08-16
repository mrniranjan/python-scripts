def factors(num):
	num = int(num)
	count = 1
	sum = 0
	while count <= num:
		y = num % count
		if y == 0:
			print count 
			sum += count
		count += 1
	return sum

num = raw_input("Enter Any number to find it's factors: ")
sum_of_factors = factors(num)

if sum_of_factors == 2 * int(num):
	print "Number %s is perfect number" % num
else:
	print "Number %s is not a perfect number" % num



