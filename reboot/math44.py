print "Enter a number and we will check if it's a prime number or not"

x = raw_input("Enter any number: ")

#/* Short Algorithm
# * We store the number in x
# * divide x by 2 ,and store it in y
# * then we check if x is divisble by 2 to y 
# * if it's divisible by any of the numbers from 2 to y then it's not a prime number*/
count = 2
y = int(x) // 2
temp = 0

while count <= y:
	temp = int(x) % count
	if temp == 0:
		print "Number %s is not prime" % x
		break
	else:
		count += 1
if temp != 0:
	print "Number %s is Prime" % x

					
