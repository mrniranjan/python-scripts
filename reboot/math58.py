'''
number = [('2', '2', '0')]

for i in number[0]:
	print i

for i in  [('2', '2', '0')]:
	#print i
	for j in i:
		print j
'''
n = [('p','q','r'),('a', 'b', 'c')]
'''
print n[0][0]
print n[0][1]
print n[0][2]
print n[1][0]
print n[1][1]
print n[1][2]
'''
for i in n:
	for j in i:
		print i
		print j
