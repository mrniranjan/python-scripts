## this program checks if sum of three odd numbers are even
# three odd numbers are given through list

def sum(n1):
	count = 0
	sum = 0 
	for i in n1:
		sum += n1[count]
		count += 1

	if sum % 2 == 0:
		return True
	else:
		return False



oddNumber = []

for i in range(1,4):
	number = raw_input("Enter Odd Number: ")
	number = int(number)
	oddNumber.append(number)

if sum(oddNumber):
	print "Sum of Numbers in %r is Even" % oddNumber
else:
	print "Sum of Numbers in %r is Odd" % oddNumber
