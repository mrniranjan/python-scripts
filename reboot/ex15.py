# Here we are importing argv feature from sys module
from sys import argv

# parameter passed to script are stored in script (command line) and filename (parameter)
script, filename = argv

# create a variable called text, which contains the handle given by 
# open function when opening the file mentioned by variable filename
txt = open(filename)

# we are printing string "here's your file %r", here
# %r is the format string which gets replaced with value stored in
# variable filename
print "Here's your file %r" % filename
#txt earlie contained handle of file opened using open call
# txt.read() function reads the contents of the file opened earlier and 
# using print function we are printing the contents to stdout
print txt.read()


# print string "Type the the filename again:"
print "Type the filename again:"
# we are creating a variable file_again which contains
# the string which we have input using raw_input
file_again = raw_input("> ")

# txt_again contains the handle given by open system call 
txt_again = open(file_again)

# print txt_again.read() prints the contents of the file that was opened and
# and read using read system call on stdou 
print txt_again.read()
