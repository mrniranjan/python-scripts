#!/usr/bin/python
from sys import argv

script, user_name = argv
prompt = '>'
print "Hi %s, I'm the %s script," % (user_name,script)
print "I would like to ask you few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright,you said %r about liking me.
you live in %r. Not sure where that is.
and you have a %r Computer, Nice.
""" % (likes,lives,computer)
