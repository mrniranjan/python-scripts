from sys import argv

prg, arg1, arg2 = argv

s1 = "we will check associative law"
a1 = int(arg1) + int(arg2)

a2 = int(arg2) + int(arg1) 

s2 = """
Associative law says %s + %s is equal to %s + %s let's check if that's true : %r
""" % (arg1 , arg2 , arg2, arg1, a1 == a2)

print s2
