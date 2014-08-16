from sys import argv

script, file1 = argv

txt = open(file1)

a1 = txt.read()

print "Enter file which contains another number:"
file2 = raw_input('> ')

file2_handle = open(file2)

a2 = file2_handle.read()

s1 = "Numbers read from %s file is %s and Number read from %s file is %s" % (file1,a1,file2,a2)

s2 = "Addition of %d and %d  numbers is : %d" % (int(a1), int(a2), int(a1) + int(a2))

print s1
print s2
