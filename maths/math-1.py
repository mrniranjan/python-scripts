#!/usr/bin/python
#get the marks obtained by 5 different subjects and find the agregate marks
# Marks are obtained from argv 
from sys import argv
script,filename = argv
target = open(filename, 'w')

sub1 = raw_input("Enter Marks for sub1: ")
sub2 = raw_input("Enter Marks for sub2: ")
sub3 = raw_input("Enter Marks for sub3: ")
sub4 = raw_input("Enter Marks for sub4: ")
sub5 = raw_input("Enter Marks for sub5: ")

total = int(sub1) + int(sub2) + int(sub3) + int(sub4) + int(sub5)
agg = total / 5

a1 = "English %d" % int(sub1)
a2 = "Mathematics %d" % int(sub2)
a3 = "Science %d" % int(sub3)
a4 = "Arts %d" % int(sub4)
a5 = "Social %d" % int(sub5)
a6 = "Total Marks %d" % total
a7 = "Aggregate %d" % agg

target.write(a1)
target.write("\n")
target.write(a2)
target.write("\n")
target.write(a3)
target.write("\n")
target.write(a4)
target.write("\n")
target.write(a5)
target.write("\n")
target.write(a6)
target.write("\n")
target.write(a7)
target.write("\n")
target.close()
