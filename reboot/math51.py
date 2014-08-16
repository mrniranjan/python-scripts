def even_odd_number(number,base):
	even = []
	while number >= base:
		val = number % base
		if val == 0:
			even.append(number)
		number -= 1
	return even

def prime_number(number):
	temp = 0
	count = 2
	val = number // 2
	while count <= 	val:
		temp = number % count
		if temp == 0:
			return 0
		else:
			count += 1
	if temp  != 0:
		return number

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



number = raw_input("Enter a number: ")
number = int(number)
print "The number you have entered has %d digits" % no_of_digits(number)

print """
Do you want to list all even & odd numbers between
1 and %d, This works if the numbers entered 
is less than 100 ,else it very difficult to
read
""" % number
check = raw_input("Type yes/no> ")

if check == 'yes':
	print "Number of even numbers from 1 to %d are: " %  number
	for i in even_odd_number(number, 2):
		print i 

	print "Number of odd numbers from 1 to %d are: " %  number
	for i in even_odd_number(number, 3):
		print i 

prime_result = prime_number(number) 
if prime_result != 0:
	print "%d is a prime number" % number
else:
	print "%d is not a prime number" % number

fac,sum = factors(number)
print "Factors of the %d are:" % number, fac
for i in fac:
	print i

if sum == number * 2:
	print "\n%d is a perfect Number" % number
else:
	print "\n%d is not a perfect Number" % number

