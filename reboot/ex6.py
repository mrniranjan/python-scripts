# we are declaring a variable x which contains 
# string "There are %d types of people" following by format matching
# string %d which gets replaced with value 10, This  string is stored in variable x
x = "There are %d types of people." % 10
# declare a variable called "binary" which contains string "binary"
binary = "binary"
#declare variable "do_not" which stores string "don't"
do_not = "don't"
# Declare variable y, which contains string "Those who know %s and those who %s", 
# %s and %s are format strings which will be replaced with value stored in variables
# 'binary' and 'do_not'
y = "Those who know %s and those who %s." % (binary, do_not)

#print value stored in variable x
print x 
# print value stored in variable y
print y

# print string "I said: %r"  %r is format string, which will be replaced with 
# value stored in variable x
print "I said: %r." % x
# print string "I also said: '%s'. " % y, %s is format string which
# will be replaced with value stored in y
print "I also said: '%s'." % y

# declare variable "hilarious who'se value is False, 
# False here is not a string but Truth value True/False"
hilarious = False

# declare a variable joke_evaluation which is storing a
# string "Isn't that joke so funny?! %r", again %r is a format string"
joke_evaluation = "Isn't that joke so funny?! %r"

# print the value stored in variable "joke_evaluation", 
# which contains a format string which will be replaced
# by value stored in the variable "hilarious"
print joke_evaluation % hilarious

# declare variable w which contains string "This is left side of ..."
w = "This is left side of..."
# declare variable e which stores the string "a string with a right side"
e = "a string with a right side."

# print the value stored in variable w and e , + combines both the strings 
print w + e
 
