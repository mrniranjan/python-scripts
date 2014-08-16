# this program checks prime factors of a number

def prime_factors(number):
	fact = []
	a = []
	count = 1
	for i in range(count, number):
		temp = number % i
		if temp == 0:
			if check_prime(i):
				fact.append(i)
	return fact

def check_prime(number):
	temp = 0
	count = 2

	if number == 2:
		return True
	else:
		val = number / 2
		if val == 1:
			return True
		else:
			while count <= val:
				temp = number % count
				if temp == 0:
					return False
				else:
					count += 1
			if temp != 0:
				return True
	
def factors(number):
        count = 1
        result = []
        while count <= number:
                temp = number % count
                if temp == 0:
                        result.append(count)
                count += 1
	return result


result1 = prime_factors(128)
result2 = factors(128)

print result1

print result2
