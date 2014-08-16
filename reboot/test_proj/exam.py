### This program is a simple examp program which asks users certain questions and 
### base on the replies , marks are alloted.
import os
from os.path import exists
import random


def make_report(data):
	filename = "report.txt"
	if exists(filename):
		fd = os.open(filename, os.O_APPEND|os.O_RDWR, 0644)
		ret = os.write(fd, data)
		ret = os.write(fd, "\n")
		os.close(fd)
	else:
		try:
			fd = os.open(filename, os.O_RDWR|os.O_CREAT, 0644)
		except IOError as e:
			if e.errno == errno.EACCESS:
				return "Permission Error"
			raise
		else:
			ret = os.write(fd, data)
			ret = os.write(fd, "\n")
			os.close(fd)

def prime_number(number):
	temp = 0
	count = 2
	val = number // 2
	while count <= val:
		temp = number % count
		if temp == 0:
			return False
		else:
			count += 1
	if temp != 0:
		return True

				
def test1(name, points_earned):
	upperbound = 1000
	n1 = random.randint(1, 1000)
	s1 = "%d is a Even or Odd Number(Type \'even\'|\'odd\'): " % n1
	print s1
	answer = raw_input("> ")
	result = even_odd_number(n1)
	if result == answer:
		points_earned += 1
	else:
		points_earned -= 1
		
	data = name + s1 +  "\t" + answer + "\t\t" +  "%d" % points_earned
	make_report(data)
	return points_earned	

def test2(name, points_earned):
	upperbound = 10
	n1 = random.randint(1, upperbound + 1)
	s1 = "Is %d a Prime Number(yes/no): " % n1
	print s1
	check = raw_input("> ")
	if prime_number(n1):
		answer = "yes"
	else:
		answer = "no"

	if check == answer:
		points_earned += 5
	else:
		points_earned -= 1
	
	data = name + s1 + "\t\t\t" + answer + "\t\t" + "%d" % points_earned
	make_report(data)
	return points_earned

	
def even_odd_number(number):
	"""This is odd number function with 
	integer as input and returns a string 'even'
	or 'odd'
	"""
	if number % 2 == 0:
		return 'even'
	else:
		return 'odd'

def start(name):
	
	### Initialize variables 
	points_earned = 1

	print """
	This is a simple test, where you will be asked simple
	questions regarding mathematics.
	"""
	points_earned = 0
	s1="Question\t\t\t\t\t\tAnswer\t\t Points Earned"
	s2="-" * 80
	make_report(s1)
	make_report(s2)

	points_earned =	test1(name, points_earned)
	points_earned = test2(name, points_earned)

def main():
	StudentName = raw_input("Enter Your Name:")
	start(StudentName)

if __name__ == '__main__':
	main()

