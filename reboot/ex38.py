ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
print "stuff = %r" % stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "Ther we go: ", stuff

print "stuff = %r" % stuff
print "Let's do some things with stuff."

print "stuff[0] is:", stuff[0]
print "stuff[1] is:", stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? Cool
print '#'.join(stuff[3:5]) # super stellar
