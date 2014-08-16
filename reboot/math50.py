#print "Enter a number:"
#num = raw_input("> ")
num = 28
base = 2
print "With base = 2"
while num >= base:
	val = num % base
	if val == 0:
		print num
	num -= 1

print "With base = 3"
num = 28
base = 3
while num >= base:
	val = num % base
	if val == 0:
		print num
	num -= 1


print "With base = 5"
num = 28
base = 5
while num >= base:
	val = num % base
	if val == 0:
		print num
	num -= 1
