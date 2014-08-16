#  print string "This program is to convert cm's to inches"
print "This program is to convert cm's to inches"

# declare variable inch which stores value 0.393701
inch = 0.393701
# declare variable cm1 which stores value 
cm1 = 25
inch1 = 30
s1 = "You know 1 cm is %0.3f inches" % inch
print s1

s2 = "what is %d cms in inches ?" 

s3 = "How many cm is %d inches ?"

s4 = "Oh it's %d inches, That's Gr8!"

s5 = "Ah so %d inches is equal to %d cms"

s6 = s2 % cm1
s7 = s3 % inch1

s8 = s4 % (cm1 * inch) 
s9 = s5 % (inch1, inch1/inch)


print s6 + s8 
print s7 + s9 
 
