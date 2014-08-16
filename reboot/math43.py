def break_numbers(stuff):
	"""This functionality will break up numbers for us."""
	numbers = stuff.split()
	return numbers

def sort_numbers(numbers):
	"""This functionality will sort numbers for us"""
	numbers.sort()
	return numbers

def add_numbers(sorted_numbers):
	"""This functionality will add numbers for us"""
	a1 = sorted_numbers.pop()
	a2 = sorted_numbers.pop()
	a3 = sorted_numbers.pop()
	a4 = sorted_numbers.pop()
	a5 = sorted_numbers.pop()
	total = int(a1) + int(a2) + int(a3) + int(a4) + int(a5)
	return total

def mean(total):
	mean = total / 5
	return mean 

stuff = raw_input("Enter 5 numbers separated by commas: ")

a1 = break_numbers(stuff)

print "Numbers have been split with , as delimiter: %s" % a1

a2 = sort_numbers(a1)

print "Numbers are sorted : %s" % a2 

a3 = add_numbers(a2)

print "Adding all the numbers we get: %d" % a3 

a4 = mean(a3)

print "Mean of Numbers is: %d " % a4 

