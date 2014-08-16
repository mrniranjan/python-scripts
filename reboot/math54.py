'''
12345
>>> 12345 % 10
5
>>> 12345 / 10
1234
>>> 1234 % 10
4
>>> 1234 / 10
123
>>> 123 % 10
3
>>> 123 / 10
12
>>> 12 % 10
2
>>> 2 / 1
2
>>> 2 / 10
0
'''
number = 12345
temp = number
x1 = []
while temp!=0:
	x1.append(temp % 10)
	temp = temp / 10
	

#print "Reverse Number: %d" % number, x1
for i in x1:
	print i 


	
	
	
	
