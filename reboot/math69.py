odd_number = "3 5 7"

print "Odd numbers between 1 to 9  numbers"
stuff = odd_number.split(' ')

print "stuff = %r" % stuff

more_stuff = ['9', '11', '17', '19', '21', '23', '25']

while len(stuff) != 10:
	count = 0
	next_one = more_stuff.pop(0)
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now" % len(stuff)


print "There we go: ", stuff

print "let's do some things with stuff."

print "stuff[0] is:", stuff[0]
print "stuff[1] is:", stuff[1]
print "stuff[-1] is:", stuff[-1]
print "Remove last item"
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[0:2])
