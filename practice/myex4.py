#!/usr/bin/python
#This program calculates simple interest using variables

principal = 4000
rate_of_interest = 5
no_of_years = 8.5

person = 'Ramesh'

print "%s borrowed %d amount, for which Simple Interest should be calculated" % (person,principal)
print "Simple interest is calculated using formula:",
print "Simple Interest = Princial (%d) * Number of years (%0.1f) * Rate of interest (%d)" % (principal, no_of_years, rate_of_interest)
#print "Which is basically %d * %0.1f * %d" % (principal, no_of_years, rate_of_interest)
print "Simple Interest for %s is: %0.2f" % (person, principal * no_of_years * rate_of_interest / 100)
