#from sys module we are importing argv module
from sys import argv
# from os.path module we are importing exists module 
from os.path import exists

# the parameters/arguments passed on the command line
# are saved in variables
script, from_file, to_file = argv

# print a string "Copying from %s to %s", %s are format specifiers
# which will be replaced with values stored in from_file and to_file
print "Copying from %s to %s" % (from_file, to_file)

# open the file mentioned in from_file and pass the handle to in_file
in_file = open(from_file)
# using in_file handle read the contents and save the contents in indata variable
indata = in_file.read()

# print a string "the input file is %d bytes long", %d will be replaced
# with output of the len(indata) function. 
print "The input file is %d bytes long" % len(indata)

# print strings to get user input whether to continue further or not
print "Does the output file existgs? %r" % exists(to_file)
print "Read, Hit RETURN to continue, CTRL-C to abort."
# raw_input asks the user input
raw_input("?")

# out_fle contains the handle returned by open function call which
# opens the file mentioned in to_file in write mode
out_file = open(to_file, 'w')
# out_file.write would write the contents saved in indata variable to file 
# mentioned in to_file
out_file.write(indata)

# print string saing all the files opened will be close
print "Alright, All done"
#out_file.close() will close the file mentioned in to_file variable
out_file.close()
#in_file.close() will close the file mentioned in from_file variable
in_file.close()

