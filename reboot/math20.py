print "Enter 4 numbers and let's check which of them is bigger"

num1 = raw_input("Enter num1:")
num2 = raw_input("Enter num2:")
num3 = raw_input("Enter num3:")
num4 = raw_input("Enter num4:")

s1 = int(num1) > int(num2)
s2 = int(num2) > int(num3)
s3 = int(num3) > int(num4)
s4 = int(num4) > int(num1)

mys = "Is %s greater than %s"

print mys % (num1, num2), s1 
print mys % (num2, num3), s2
print mys % (num3, num4), s3
print mys % (num4, num1), s4


