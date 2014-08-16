from sys import argv
script, file, sname = argv

def student_report(studentName,filename):
	s1 = "...........Student Report Card............"
	s2 = "Enter student Marks for the following subjects"
	print s1 + "\n" + s2
	english = raw_input("English: ")
	science = raw_input("Science: ")
	maths = raw_input("Maths: ")
	hindi = raw_input("Hindi: ")
	
	total_marks = int(english) + int(science) + int(maths) + int(hindi)
	avg = total_marks  / 4
	
	s3 = """
	\tReport card of %s
	\tEnglish: %s
	\tScinece: %s
	\tMaths: %s
	\tHindi: %s
	\t...............
	\tTotal: %d
	\t\n
	\tAverage: %d
	\t...............
	""" % (studentName, english, science, maths, hindi, total_marks, avg)
	
	target = open(filename,'w')
	target.write(s3)
	target.close()

	target = open(filename)
	print target.read()
	target.close()

student_report(file,sname)

	
	

