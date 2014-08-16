print "Find factors of the number:"
num = raw_input()
count = 1
#sum = 0
while count <= int(num):
	y = int(num) % count 
	if y == 0:
		print count
		#sum += count
	count += 1


#print sum
