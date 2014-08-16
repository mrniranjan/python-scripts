number = 11
count = 1
factors = []
while count <= number:
	temp = number % count
	if temp == 0:
		factors.append(count)
	count += 1

for number in factors:
	print number
