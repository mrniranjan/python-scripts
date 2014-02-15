#!/usr/bin/python
def reverse_of_number(num):
	a1 = num % 10 
	num = num / 10
	a2 = num % 10 
	num = num / 10
	a3 = num % 10 
	num = num / 10
	a4 = num % 10
	num = num / 10
	a5 = num % 10
	
	val = a1 * 10000 + a2 * 1000 + a3 * 100 + a4 * 10 + a5
	return val

rev = reverse_of_number(int(raw_input("Enter a 5 digit number: ")))
print rev

