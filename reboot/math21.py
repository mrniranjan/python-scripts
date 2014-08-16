print "This program reverses a number given"

number = raw_input("Enter any 5 digit number:")
num = int(number)

n1 = num % 10
num = num / 10
n2 = num % 10
num = num / 10
n3 = num % 10
num = num / 10
n4 = num % 10
num = num / 10
n5 = num % 10

num = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5

s1 = """
Now the %s that was initially given is now:\t %d
""" % (number, num)
print s1


