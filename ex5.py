#!/usr/bin/python

# We are declaring variable "x" which contain string "There are %d types of people." , %d is replaced with 10
x = "There are %d types of people." % 10

# declare a varilable binary with value(String) "binary"
binary = "binary"
# Declare variable "do_not" , wich contains string "don't"
do_not = "don't"

# Declare variable y which contains string "Those who know %s and those who %s.", %s and %s are replaced by binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# we are printing variable x
print x 
# we are print variable y (which in-turn prints string stored in y)
print y

# print string "I said: %r.", % %r will be replaced with the value stored in x 
print "I said: %r." % x
# print string "I also said: '%s'", % y , %s will be replaced by value stored in y
print "I also said: '%s'." % y

# declare variable hilarious with value = False
hilarious = False
# declare variable joke_evaluation, which contains string value "Isn't that joke so funny?! %"
joke_evaluation = "Isn't that joke so funny?! %r"

# print value stored in joke_evaluation, when printing the %r in the string will be replaced by hilarious
print joke_evaluation % hilarious

# declare variable w which contains string "This is left side of the ...." 
w = "This is left side of the ...." 
# declare variable e which contains string "a string with a right side."
e = "a string with a right side."

#print string stored in w and e togother. 
print w + e 
