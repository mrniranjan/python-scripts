#!/usr/bin/python 
#This program converts Centimeters to Meters

cm = 'Centimeters'
me = 'Meters'
print " This Program Converts '%s' to '%s' " % (cm,me)
print "*"*50

print " First How many '%s' is equal to '%s' ? " % (cm, me), 
print " It's %d '%s' is equal %0.2f '%s'" % (1,cm,0.01,me)

val_cm = 29280 
val_me = 15

print " We will Convert %d %s to %s " % (val_cm, cm, me)

val_me_conv = val_cm * 0.01 

print " %d %s is %0.2f %s " % (val_cm, cm, val_me_conv, me)

print " So is %0.2f %s greater than %d %s " % (val_me_conv, me, val_me, me), val_me_conv > val_me 

print "*"*50

