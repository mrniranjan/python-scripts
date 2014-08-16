# This number check if a given number is divisible by numbers from 2 to 10
def divisibility():
	n1 = 18
	result=[]
	for i in range(1, 19):
		if (n1 % i) == 0:
			result.append(i)
	print result
		

divisibility()
	
