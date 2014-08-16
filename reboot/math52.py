number = 1234567890
temp = number
val = 0 
count = 1
# divide the number and get the quotiont

'''x = number % count
if x == 0:
	val += 1
	count = count * 10
	x = number % count
	if x == 0:
		val += 1
		count = count * 10
		x = number % count
		if x == 0:
			val += 1
			count = count * 10 
			x = number % count
		
'''
x = number / count
while x != 0:
	val +=1
	count = count * 10
	x = number / count
	

print val	
