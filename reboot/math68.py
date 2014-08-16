def prime_number(number):
	temp = 0
	count = 2
	val = number // 2
	while count <= 	val:
		temp = number % count
		if temp == 0:
			return False
		else:
			count += 1
	if temp  != 0:
		return True

def range_prime(number):
	result = []
	for i in range(1, number+1):
		temp = 0
		count = 2
		if i == 2:
			result.append(2)
		else:
			val = i // 2
			while count <= val:
				temp = i % count
				if temp == 0:
					break
				else:
					count +=1
			if temp != 0:
				result.append(i)
	return result
	
def factors(number):
	count = 1
	sum = 0 
	factors = []
	while count <= number:
		temp = number % count
		if temp == 0:
			factors.append(count)
			sum += count
		count += 1
	return factors, sum

def no_of_digits(number):
	temp = 1
	count = 0
	x = number / temp
	while x != 0:
        	count +=1
	        temp = temp * 10
        	x = number / temp
	return count



#number = raw_input("Enter a number: ")
#number = int(number)
#print "The number you have entered has %d digits" % no_of_digits(number)
#result = range_prime(number) 

#print result
'''
prime_result = prime_number(number)
print "prime result = %d" % prime_result

if prime_result:
	print "%d is a prime number" % number
else:
	print "%d is not a prime number" % number

fac,sum = factors(number)
print "Factors of the %d are:" % number, fac

if sum == number * 2:
	print "\n%d is a perfect Number" % number
else:
	print "\n%d is not a perfect Number" % number
'''


