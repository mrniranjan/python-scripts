#This program shows the greatest prime numbers between 1 to 10
def primes():
#	n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	result = []
	for i in range(1, 101):
		temp = 0
		count = 2
		val = i // 2
		while count <= val:
			temp = i % count
			if temp == 0:
				break
			else:
				count += 1
		if temp != 0:
			result.append(i)
	print result
	value = greatest_primes(result)
	print value

def greatest_primes(result):
	count = 0
	length = len(result)
	currentlarge = result[count]
	for i in result:
		count += 1
		if count <= length - 1:
			if currentlarge < result[count]:
				currentlarge = result[count]
	return currentlarge


primes()
