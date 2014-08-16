# this program check the Comman factors between 2 Numbers:

def factors(number):
	count = 1
	result = []
	print "Number = %d" % number
	upperbound = number + 1
	for i in range(1, upperbound):
		if (number % i) == 0:
			result.append(i)
	return result	

def common_factors(n1, n2):
	result = []
	for element in n1:
		if element in n2:
			result.append(element)
	return result

def greatest_common_factor(common_factors):
	count = 0
	length = len(common_factors)
	current_largest = common_factors[count]
	for i in common_factors:
		count += 1
		if count <= length - 1:
			if current_largest < common_factors[count]:
				current_largest = common_factors[count]
	return current_largest	

n1 = raw_input("Enter Number: ")
n2 = raw_input("Enter Number: ")

n1 = int(n1)
n2 = int(n2)

result1 = factors(n1)
result2 = factors(n2)

print result1
print result2

result3 = common_factors(result1,result2)
print result3

result4 = greatest_common_factor(result3)
print result4
