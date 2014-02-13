#!/usr/bin/python

from sys import argv

script,filename = argv
hra_per = 20 
da_per = 40 

name_of_employer = raw_input("Name of the Employer: ")
basic_salary = raw_input("Basic Salary: ")

print "HRA is %d percent of Basic Salary %d" % (hra_per,int(basic_salary))
print "DA is %d percent of Basic Salary %d" % (da_per, int(basic_salary))

hra = int(basic_salary) * 20 / 100
da = int(basic_salary) * 40 / 100 
gs = int(basic_salary) + hra + da

x = "Employer Name %s" % name_of_employer
y = "HRA is %0.2f" % hra
z = "DA is %0.2f" % da

A = "Gross Salary of %s is %0.2f" % (name_of_employer, gs)


target = open(filename, 'w') 

target.write(x)
target.write("\n")
target.write(y)
target.write("\n")
target.write(z)
target.write("\n")
target.write(A)
target.write("\n")
target.close()





