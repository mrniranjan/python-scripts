#!/usr/bin/python
#This program converts centimeters to Inches

# Declared variable cm which contains string Centimeters
cm = 'Centimeters'

# Declared variable inch which contains string "inches"
inch = 'Inches'

# Declared variable var1cm which has value 100
var1cm = 100

#Declare variable var2inch which has value 25
var2inch = 25

#Printing string which contains format string 
print "This program converts %s to %s" % (cm,inch)

#Printing Asteriks * 45 times
print "*"*45

# Print string containing format string 
print "1 %s is equivalent %0.6f %s" % (cm,0.393701,inch)

# print string which contains format string
print "%d %s would be %0.2f %s" % (12,cm,12*0.393701,inch)

# print string which also contains format string
print "let's check if %d %s is more than %d %s in length" % (var1cm,cm,var2inch,inch)

# Declare variable x which contains a string which also contains format string 
x =  "let us first convert %d %s to %s"

# printing  variable x with format paramters passed as defined in the string
print x % (var1cm,cm,inch)

# Declare variable y which contains format string 
y = "%d %s is %0.2f %s"

# print variable y with format parameters passed as defined in the string 
print y % (var1cm,cm,100 * 0.393701,inch)

# print string where we are checking if 100 cm's when converted to inches is greater than 25 inches
print "So is %0.2f greater than %d inch: " % (100 * 0.393701,var2inch), 100 * 0.393701 > 25 

# print Asterik * 45 times
print "*"*45
