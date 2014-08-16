from sys import argv

script, arg1, arg2, arg3, arg4 = argv

print "You have entered 4 numbers:%s, %s, %s and %s" % (arg1, arg2, arg3, arg4)

myout = int(arg1) + int(arg2) + int(arg3) + int(arg4)

print "sum of %s + %s + %s + %s is: %d"  % (arg1, arg2, arg3, arg4, myout)

