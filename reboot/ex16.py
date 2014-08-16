# from the sys module we are importing argv feature
# which takes parameters from command line
from sys import argv

# the command line arguments are unpacked to variables 
# of this program
script, filename = argv

# we are printing the string "we're going to erase %r", % filename
# Format string %r is replaced with value stored in variable filename
##print "We're going to erase %r." % filename
#again we are printing strings nothing much
##print "If you don't want that, hit CTRL-C(^C)."
##print "If you do want that hit RETURN."

s1 = """
If you don't want that, hit CTRL-C(^C)
if you do want that hit RETURN."
"""

print s1
# we take user input , and it shows ? as prompt
raw_input("?")

# we are printing string to stdout
print "Opening the file..."
# we are are creating a variable target
# which consits the handle (or a method) , given by the function
#open which opens a name of the file stored in variable filename and
# it opens in write mode
target = open(filename, 'w')

# printing a string 
print "Truncating the file. Goodbye"

# target variable consits a method to access the file stored in filename
# we are using target with truncate function to delete all the lines in the file
# (the filename is stored in filename variable)
target.truncate()

# print a string to stdout
print "Now i am goint to ask you for three lines."

# we are asking a user input and input text is stored in variable line1
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

# printing a string to stdout
print "I'm going to write these to the file."

# using the target handle we are accessing write function to write something to file
# the contents to be written is passed as parameter to write function
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# print a string to stdout
print "And finally, we close it"
# using the target handle we call close function and closing the file that was opened
target.close()
