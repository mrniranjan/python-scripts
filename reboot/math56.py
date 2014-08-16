def calculate_marks():
	subjects = ['Mathematics', 'Science', 'Social Studies', 'Hindi']
	marks = {}
	count = 0
	report = {}
	for i in subjects:
		the_sub = subjects[count]
		marks[the_sub] = raw_input("Enter Marks for "+str(the_sub)+" :")
		count += 1
	print marks
	#{'Social Studies': '32', 'Mathematics': '51', 'Hindi': '32', 'Science': '12'}
	for i in marks:
		if marks[i] > 30 and marks[i] < 40:
			report[i] = "Just Pass"
		elif marks[i] > 30 and marks[i] < 40:
			report[i] = "Third Class"
		elif marks[i] > 40 and marks[i] < 60:
			report[i] = "Second Class"
		elif marks[i] > 60 and marks[i] < 70:
			report[i] = "First Class"
		elif marks[i] > 70 and marks[i] < 90:
			report[i] = "Distinction"
		else:
			report[i] = "Fail"
	print report
		
calculate_marks()
