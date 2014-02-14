def simple_interest(*args):
	person,principal,rate_of_int,no_of_users = args
	print "%s borrowed %d amount, for which simple interest should be calculated" % (person,principal)
	print "Simple interest is calculated using formula:",
	print "Simple interest = Principal (%d) * Number of years (%0.1f) * Rae of interest (%d)" % (principal,no_of_users, rate_of_interest)
	print "Simple interest for %s is: %0.2f" % (person, principal * no_of_years * rate_of_int / 100)

name = "Ramesh"
principal = 4000
rate_of_interest = 5
no_of_years = 8.5

simple_interest(name,principal,rate_of_interest,no_of_years)
