from sys import argv

script, filename = argv

print "....Student Report Card...."

print "opening %s file in write mode" % filename
target = open(filename,'w')

student_1 = raw_input("Enter student name:")

print "Enter marks for below subjects:"

english = raw_input("English:")
science = raw_input("science:")
maths = raw_input("Maths:")
hindi = raw_input("Hindi:")

totalmarks = int(english) + int(science) + int(maths) + int(hindi)
avg = totalmarks / 4

s1 = "Report card of %s" % student_1
s2 = "." * 20
s3 = "English: %r" % english
s4 = "Science: %r" % science
s5 = "Mathematics: %r" % maths
s6 = "Hindi: %r" % hindi
s7 = "." * 20 
s8 = "Total: %d" % totalmarks
s9 = "." * 20
s10 = "Average: %d" % avg



target.write(s1)
target.write("\n")
target.write(s2)
target.write("\n")
target.write(s3)
target.write("\n")
target.write(s4)
target.write("\n")
target.write(s5)
target.write("\n")
target.write(s6)
target.write("\n")
target.write(s7)
target.write("\n")
target.write(s8)
target.write("\n")
target.write(s9)
target.write("\n")
target.write(s10)
target.write("\n")
target.close()

target = open(filename)
print target.read()


print "Closing the file %s" % filename
target.close()


