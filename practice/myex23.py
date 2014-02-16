#!/usr/bin/python
# This program converts Pounds to Kilograms
print "This program converts Pounds to kilograms"
print "*" * 50
print "Enter the Weight(lbs)" 
pnd = raw_input('-->')
unit = 0.453592
#1 pound is equivalent to 0.453592 kilograms
kg = int(pnd) * unit 

print "You are %d kilograms" % kg 


