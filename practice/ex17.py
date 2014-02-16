#!/usr/bin/python

# We are importing feature "argv" from the set of features(module) sys
from sys import argv
# we are importing feature "exists" from set of features(modules) os.path
from os.path import exists

# Passing arguments that will be saved in argv, filename and name of the script
script,from_file,to_file = argv
# Display a message of which file is copied as which file
print "Copying from %s to %s" % (from_file,to_file)

# we are opening the source file and returned file object is stored in in_file
in_file = open(from_file)
# Read the contents of the source and copy the contents to variable called indata
indata = in_file.read()

#we are printing size of the data that is stored in indata which is calculated using len() function
print "The input file is %d bytes long" % len(indata)
# print the contents of source file
print indata


#we are checking if the destination file exists using exists() function that is part of the os.path module
print "Does the output file exists? %r" % exists(to_file)
# we are checking with user if he want's to continue copying or abort
print "Ready, hit Return to Continue, CTRL-C to abort"
# input is captured by raw_input but not saved any where
raw_input()

# we are opening the destination file(creating if the file doesn't exist) 
out_file = open(to_file, 'w')
#return object is saved in out_file and then used to write in to the file 
# we are writing contents of indata to the destination file
out_file.write(indata)

#print string "Allright all done
print "Alright, all done."

# close both the source and destination files
out_file.close()
in_file.close()
