#!/usr/bin/python
# This program Calculates Simple Interest , and it gets it 
#inputs from the user using raw_input()

print "\tName: ",
name = raw_input()
print "\tPrincipal Amount: ",
p_amount = raw_input()
print "\tInterest Rate: ",
int_rate = raw_input()
print "\tNumber of Years: ",
no_years = raw_input()

si_amt = float(p_amount) * int(no_years) * float(int_rate) / 100

x = "\tSimple Interest for Amount %0.3f"
y = "\n\twith Rate of Interest %0.2f"
z = "\n\tfor %d Years is: %0.2f"

print "\tSimple Interest Calculation for %r" % (name)
print "\t","*" * 45
print "\n"
print x % float(p_amount) + y % float(int_rate),
print z % (int(no_years),int(si_amt))
print "\n"
print "\t", "*" * 45


