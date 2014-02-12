#!/usr/bin/python

### From the features(module) sys We are using a particular feature(module) 
# called argv
from sys import argv

### To argv, we are saying to argv we will take 2 arguments
#one if the name of the program and 2nd is a string
#first value entered is stored in variable called script
#2nd value entered is stored in variable filename
script, filename = argv

# We are using a builtin function called open , which takes a string
#as it's argument, it assumes that this string is a name of the file
#in current working directory 
# The function returns a file object, This file object is stored in 
# variable called text
txt = open(filename)

#We are printing a string "here's your filename : Name of the filename(string)
#that was passed as argument
print "Here's your filename %r" % filename

#here txt variable got a file object , this object can be given certain
#instruction , one of the instruction is to read the contents of the file 
#that has been sent to open function
print txt.read()

# we are print a string called "Type the filename again:"
print "Type the Filename again:"
# the input is read using raw_input and saved in variable file_again
file_again = raw_input("> ")
#the string that has been given is passed to open function , which returns
# a file object that is saved in txt_again varible
txt_again = open(file_again)

# and we are reading the contents of the name of the file stored in file_again
print txt_again.read()

