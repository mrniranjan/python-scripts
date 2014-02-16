#!/usr/bin/python 
#This program finds greatest of 2 numbers

print "Finding greatest of 2 Numbers" 

x = 475320
y = 9847215
z = 97645310

print "Which of these Numbers are geatest\n %d %d %d" % (x,y,z)
print "Let's check if %d > %d" % (x,y), x > y 
print "Let's check if %d > %d" % (x, z), x > z
print "Which makes %d the smallest" % x 
print "Let's check if %d > %d" % (y,z), y > z
print "Let's check if %d > %d" % (z,y), z > y
print "So %d is greater of all 3 numbers %d,%d,%d" % (z,x,y,z)

print "Let's check if %d > %d > %d" % (x, y, z), x > y > z
print "Let's check if %d < %d < %d" % (x, y, z), x < y < z
print "Let's check if %d <= %d > %d" % (x, y, z), x <= y > z

