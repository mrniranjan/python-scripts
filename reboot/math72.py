#!/usr/bin/env python
"""
	This program creates a dictionary , where key represents Number , 
	it has 2 values , one list  and another number. 
	The list correponds to it's factors, and Number corresponds to 
	Number of factors
"""

def factors(num):
	""" This function returns Factors of a numbers. 
	Output returned is in the form of list
	"""
	Factors = []
	count = 0
	for i in range(1, num+1):
		temp = num % i
		if temp == 0:
			count += 1	
			Factors.append(i)
	
	return Factors, count


def main():
	""" Main function calling other functions"""


	result,count = factors(5)
	dict = {}
	
	for j in range(0, len(result)):
		dict.setdefault(5, []).append(result[j])

	print dict
	#print result
	#print count


if __name__ == '__main__':
	main()
