#!/usr/bin/python 
#This Program converts Kilometers to Centimeters

#Local variables
km = "KiloMeters"
cm = "Centimeters"
me = "Meters"

#Print what the program Does
print "\tThis Program Converts %s to %s" % (km,cm)
print "*" * 65

print "\tConvert %s to %s first" % (km,me)

x = "%d %s is %d %s" 

print "\t" + x % (1,km,1000,me)
print "\t" + x % (1,me,100,cm)
print "\t" + "So " + x % (1,km,100 * 1000,cm)
## Lets ask the users 

km_val = raw_input("Enter a Number:")
print "\t" + x % (int(km_val), km, int(km_val) * 100 * 1000, cm) 
print "*" * 65






