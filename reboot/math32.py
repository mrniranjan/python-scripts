from sys import argv

script, file1, file2, file3 = argv

a1 = open(file1)
a2 = open(file2)
a3 = open(file3)

sum = int(a1.read()) + int(a2.read()) + int(a3.read())

print sum
