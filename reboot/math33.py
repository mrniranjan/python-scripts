from sys import argv

script, file1, file2, file3, file4, file5 = argv

a1 = open(file1)
a2 = open(file2)
a3 = open(file3)
a4 = open(file4)
a5 = open(file5)

num1=a1.read()
num2=a2.read()
num3=a3.read()
num4=a4.read()
num5=a5.read()

sum = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
avg = sum/5
print "Average of %s, %s, %s, %s, %s is: %d" % (num1, num2, num3, num4, num5, avg)

