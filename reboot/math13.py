num1 = 92
num2 = 392
num3 = 4456
num4 = 89742
print "let's find out which of the below numbers are bigger"
print "         %d, %d, %d, %d" % (num1, num2, num3, num4)

result1 = num1 > num2 
result2 = num2 > num3
result3 = num3 > num4 
result4 = num4 > num1

mys = "Of numbers %d and %d , Is %d greater than %d:" 

s1 = mys % (num1, num2, num1, num2)
s2 = mys % (num2, num3, num2, num3)
s3 = mys % (num3, num4, num3, num4)
s4 = mys % (num4, num1, num4, num1)

print s1 , result1
print s2 , result2
print s3 , result3
print s4 , result4

