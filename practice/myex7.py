#!/usr/bin/python

# This Program converts Meters to Kilometers

print " This program Converts Meters to Kilometers " 
print "*"*45
me = 'Meters'
km = 'KiloMeters'
conv = 1000

print ' So How many %s make 1 %s ?' % (me,km),
print " It's 1 %s is %d %s " % (km,conv,me)

to_be_conv = 1784 

print ' we will convert %d %s to %s ' % (to_be_conv,me,km) 

in_km = to_be_conv / conv 

print ' %d %s is %0.4f %s ' % (to_be_conv,me,in_km,km) 
print "*"*45


