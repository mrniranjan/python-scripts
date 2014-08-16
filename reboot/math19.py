print "let do some examples related to simple interest"

principal=2500
nofyrs=12
interest=5

si= principal * nofyrs * interest / 100
print si

principal = raw_input("Principal Amount: ")
interest = raw_input("Interest: ")
nofyrs = raw_input("Number of years: ")

si = int(principal) * int(nofyrs) * int(interest) / 100 

s1 = """
Simple Interst for Principal amount %s,
with Interest of %s for %s years is: %d 
""" % (principal, interest, nofyrs, si)

print s1
