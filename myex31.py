#!/usr/bin/python
from sys import argv
#from os.path import exists

def subj(*args):
	name = args
	print "Enter Marks for %s" % name
	maths = int(raw_input("Enter Marks for Mathematics:"))
	science = int(raw_input("Enter Marks for Science:"))
	english = int(raw_input("Enter Marks for English:"))
	social = int(raw_input("Enter Marks for Social Studies:"))
	hindi = int(raw_input("Enter Marks for Hindi:"))
	total = maths + science + english + social + hindi
	return name,maths,science,english,social,hindi,total

def report(name,maths,science,english,social,hindi,total):
	#name,maths,science,englisoh,social,hindi,total = args
	filename = "report.txt"
	target = open(filename, 'w')
	x1 = """
	Report Card for %s
	Mathematics: %d
	Science    : %d
	English    : %d
	Social     : %d
	Hindi      : %d
	Total	   : %d
	""" % (name,maths,science,english,social,hindi,total)
	target.write(x1)
	target.write("\n")
	target.close()
	

script,name = argv
name,maths,science,english,social,hindi,total = subj(str(name))
report(str(name),maths,science,english,social,hindi,total)
