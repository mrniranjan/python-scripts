#!/usr/bin/python

print "How old are you ?",
age = raw_input(':')
print "how tall are you ?",
height = raw_input(':')
print "How much do you weigh?",
weight = raw_input(':')

print "So you are %r old %r tall and %r heavy" % (age,height,weight)


### raw_input is one of python's builtin functions, i.e we don't have to import any module
##optios:
#raw_input([prompt])
#example raw_input(:)

