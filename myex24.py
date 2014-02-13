#!/usr/bin/python
# volume of a cylinder:  3.14 * r * h
from sys import argv 

script, radius, height = argv

print "Radius of cylinder = %d" % int(radius)
print "Height of cylinder = %d" % int(height)

print "Volume of cylinder is: %0.2f" % (3.14 * int(radius) * int(height))



