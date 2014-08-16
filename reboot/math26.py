from sys import argv

script, arg1, arg2 = argv

s1 = "The 2 numbers that were entered were %r and %r" % (arg1, arg2)
s2 = "Are the 2 numbers equal : %r " % (int(arg1) == int(arg2))
s3 = "Division of %r and %r is : %d " % (arg1, arg2, int(arg1)/int(arg2))

print s2 + s3
