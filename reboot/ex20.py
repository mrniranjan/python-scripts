# we are importing feature argv from sys module
from sys import argv

# all the command line arguments that were passed
# have been saved in variables
script, input_file  = argv

# declare a function called print_all
# which takes a parameter , which is a file handle(object)
# called f. 
def print_all(f):
# we are calling read function using file handle to read all the
# contents of file that is referenced by file handle "f"
	print f.read()

# declare a function called rewind which takes a file handle 
# as it's argument
def rewind(f):
# print f.seek(0) , here we are calling seek method/function with
# argument 0, which causes to file handle to start pointint to starting
#line of the file. 
	f.seek(0)

# declare a function called print_a_line which takes 2 parameters
# line_count, f: line_count is variable and f is file handle to the file
def print_a_line(line_count, f):
# here we are printing the contents of the output of f.readline and line_count
# f.readline() function read's 1 line at a time. 
	print line_count, f.readline()


# we are creating a variable called current_file which contains the file
# handle returned by open call which takes parameter input_file which contains
# the name of the file to be opened 
current_file = open(input_file)

#print string "First let's print the whole file:\n:"
print "First let's print the whole file:\n"

# call print_all function with parameter (current_file) passed
print_all(current_file)

#print string
print "Now let's rewind, kind of like a tape."

# after reading the whole file , we are asking the 
# pointer which is currently at the last line to go back to first line
rewind(current_file)

# print string
print "Let's print three lines:"

# create a variable current_line 
current_line = 1
# call print_a_line function with variables current_line and current_file
# current_line is a variable which currently consists value 1 
# current_file is a file handle 
print_a_line(current_line, current_file)

# current_line is incremented by 1
current_line += 1
# call print_a_line function with 2 arguments
# current_line = 2 
# current_file = file handle
print_a_line(current_line, current_file)

# current_linei s incremented by 1
current_line += 1
# call print_a_line function with 2 arguments
# current_line = 3
# current_file = file handle
print_a_line(current_line, current_file)
